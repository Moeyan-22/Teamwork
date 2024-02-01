#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, CommandBoolRequest, SetMode, SetModeRequest
import threading
from std_msgs.msg import UInt8
import subprocess 

class AutoController:

    def __init__(self):
        # Global variables
        self.current_state = State()
        self.pose = PoseStamped()
        self.arming_client = None
        self.set_mode_client = None
        self.local_pos_pub = None
        self.rate = None
        self.shutdown_flag = False  
        self.mode = 1
        self.started = False
        self.drone_x = 0
        self.drone_y = 0
        self.drone_z = 0
        self.bag_process = None  

    def local_pose_callback(self, data):
        self.drone_x = data.pose.position.x
        self.drone_y = data.pose.position.y
        self.drone_z = data.pose.position.z

    def start_rosbag_recording(self, topics):
        bag_file = "/home/jetson/Desktop/teamwork.bag"
        rosbag_cmd = ["rosbag", "record", "-O", bag_file] + topics
        self.bag_process = subprocess.Popen(rosbag_cmd)
        rospy.loginfo("Recording rosbag...")

    def stop_rosbag_recording(self):
        if self.bag_process is not None:
            self.bag_process.terminate()
            rospy.loginfo("Recording stopped.")
        else:
            rospy.logwarn("No rosbag process to terminate.")

    def mode_callback(self, data):
        self.mode = data.data
    
    def state_callback(self, data):
        self.current_state = data

    def send_setpoints(self):
        start_time = rospy.Time.now()

        while not rospy.is_shutdown() and not self.shutdown_flag:
            elapsed_time = rospy.Time.now() - start_time
            #rospy.loginfo(f"Current Pose - X: {self.drone_x}, Y: {self.drone_y}, Z: {self.drone_z}")
            if elapsed_time < rospy.Duration(20.0):
                # Send setpoints with mode 1
                self.pose.pose.position.x = self.current_x
            else:
                # Change x value to 2 and continue sending setpoints with mode 3
                self.pose.pose.position.x = self.current_x + 2

            # Send setpoints
            self.local_pos_pub.publish(self.pose)
            self.rate.sleep()

            if elapsed_time > rospy.Duration(30.0):
                # Initiating landing after 25 seconds
                self.shutdown_flag = True
                land_mode = SetModeRequest()
                land_mode.custom_mode = 'AUTO.LAND'

                try:
                    self.set_mode_client.call(land_mode)
                    rospy.loginfo("Initiating landing...")

                    # Wait for the landing to complete (adjust the duration as needed)
                    rospy.sleep(10)

                    # Disarm the vehicle
                    arm_cmd = CommandBoolRequest()
                    arm_cmd.value = False

                    try:
                        self.arming_client.call(arm_cmd)
                        rospy.loginfo("Vehicle disarmed")
                    except rospy.ServiceException as e:
                        rospy.logerr(f"Service call to cmd/arming failed: {e}")

                    # Break out of the loop to stop sending setpoints
                    break
                except rospy.ServiceException as e:
                    rospy.logerr(f"Service call to set_mode failed: {e}")


    def main(self):
        rospy.init_node("offb_node_py")

        # Subscribe to the mode topic
        rospy.Subscriber("/mavros/rc/mode", UInt8, self.mode_callback)

        state_sub = rospy.Subscriber("mavros/state", State, callback=self.state_callback)

        rospy.Subscriber("/mavros/local_position/pose", PoseStamped, self.local_pose_callback)

        self.local_pos_pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped, queue_size=10)

        rospy.wait_for_service("/mavros/cmd/arming")
        self.arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)

        rospy.wait_for_service("/mavros/set_mode")
        self.set_mode_client = rospy.ServiceProxy("mavros/set_mode", SetMode)

        # Setpoint publishing MUST be faster than 2Hz
        self.rate = rospy.Rate(20)

        # Wait for Flight Controller connection
        while not rospy.is_shutdown() and not self.current_state.connected:
            self.rate.sleep()

        setpoints_thread = threading.Thread(target=self.send_setpoints)

        while not rospy.is_shutdown():
            if self.started == False and self.mode == 3:
                    
                    self.start_rosbag_recording(["/mavros/local_position/pose", "/mavros/setpoint_position/local"])
                    self.started = True
                    
                    self.current_x = self.drone_x
                    self.current_y = self.drone_y
                    self.current_z = self.drone_z

                    rospy.loginfo(f"Current Pose - X: {self.current_x}, Y: {self.current_y}, Z: {self.current_z}")


                    self.pose.pose.position.x = self.current_x
                    self.pose.pose.position.y = self.current_y
                    self.pose.pose.position.z = self.current_z + 2

                    # Start a new thread for sending setpoints
                    setpoints_thread.start()

                    offb_set_mode = SetModeRequest()
                    offb_set_mode.custom_mode = 'OFFBOARD'

                    arm_cmd = CommandBoolRequest()
                    arm_cmd.value = True

                    last_req = rospy.Time.now()

                    while not rospy.is_shutdown():
                        if self.current_state.mode != "OFFBOARD" and (rospy.Time.now() - last_req) > rospy.Duration(5.0) and not self.shutdown_flag:
                            if self.set_mode_client.call(offb_set_mode).mode_sent:
                                rospy.loginfo("OFFBOARD enabled")

                            last_req = rospy.Time.now()
                        else:
                            if not self.current_state.armed and (rospy.Time.now() - last_req) > rospy.Duration(5.0) and not self.shutdown_flag:
                                if self.arming_client.call(arm_cmd).success:
                                    rospy.loginfo("Vehicle armed")

                                last_req = rospy.Time.now()

                        self.local_pos_pub.publish(self.pose)

                        self.rate.sleep()

                        if self.started == True and self.mode != 3: 
                            self.stop_rosbag_recording()
                            break
            else:
                pass

                

        # Graceful shutdown: Wait for the setpoints thread to finish
        self.shutdown_flag = True

if __name__ == "__main__":
    try:
        auto_controller = AutoController()
        auto_controller.main()
    except rospy.ROSInterruptException:
        pass
    except Exception as e:
        rospy.logerr("Error in main: {}".format(str(e)))

