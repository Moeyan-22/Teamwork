#!/usr/bin/env python3

import rospy
from mavros_msgs.msg import RCIn
from std_msgs.msg import UInt8
from geometry_msgs.msg import PoseStamped

class RCListener:
    def __init__(self):
        self.channel_6 = 0
        self.channel_7 = 0
        self.channel_8 = 0
        self.channel_8_past = 0
        self.block = 0
        self.pose = 0
        self.mode = 1  # 1 is full manual, 2 is assisted manual, 3 is full auto
        self.action = 0  # 0 no action, 1 fully extend, 2 fully retract,
        self.x = 0
        self.x_past = 0
        self.y = 0
        self.z = 0
        self.orientation_z = 0
        self.orientation_w = 0
        self.actuator_extended = False
        self.mode_publisher = rospy.Publisher('/mavros/rc/mode', UInt8, queue_size=10)
        self.action_publisher = rospy.Publisher('/mavros/rc/action', UInt8, queue_size=10)

    def rc_callback(self, data):
        # RC channels start from index 0
        self.channel_6 = data.channels[5] if len(data.channels) > 5 else 0
        self.channel_7 = data.channels[6] if len(data.channels) > 6 else 0
        self.channel_8 = data.channels[7] if len(data.channels) > 7 else 0

        # rospy.loginfo("RC Channel 6: {}, Channel 7: {}, Channel 8: {}".format(
        # self.channel_6, self.channel_7, self.channel_8))
    
    def pose_callback(self, data):
        # Access the pose from PoseStamped message
        pose_msg = data.pose

        # Extract the desired pose information (modify as needed)
        self.x = pose_msg.position.x
        self.y = pose_msg.position.y
        self.z = pose_msg.position.z
        self.orientation_z = pose_msg.orientation.z
        self.orientation_w = pose_msg.orientation.w

    def block_callback(self, data):
        self.block = data.data

    def start(self):
        rospy.init_node('main_controller', anonymous=False)
        rospy.Subscriber("/mavros/rc/in", RCIn, self.rc_callback)
        rospy.Subscriber("/aruco/pose", PoseStamped, self.pose_callback)
        rospy.Subscriber("/aruco/block", UInt8, self.block_callback)

        rate = rospy.Rate(10)

        while not rospy.is_shutdown():

            if self.channel_6 == 1934:
                self.mode = 1
            elif 1094 < self.channel_6 < 1934:
                self.mode = 2
            elif self.channel_6 == 1094:
                self.mode = 3

            if self.channel_7 == 1934 and self.actuator_extended == False:
                self.channel_8_past = 0
                self.action = 1
                self.actuator_extended = True
            elif self.channel_7 == 1094 and self.actuator_extended == True:
                self.action = 2
                self.actuator_extended = False

            if self.channel_8 == 1934 and self.channel_8_past == 0:
                self.channel_8_past = 1
            elif self.channel_8 == 1094 and self.channel_8_past == 1:
                self.action = 0

            # Publish the mode information to the topic
            mode_msg = UInt8()
            mode_msg.data = self.mode
            self.mode_publisher.publish(mode_msg)

            # Publish the action information to the topic
            action_msg = UInt8()
            action_msg.data = self.action
            self.action_publisher.publish(action_msg)

            if self.mode == 2 or self.mode == 3:
                
                if self.x != self.x_past and self.actuator_extended == False:
                    self.action = 1
                    self.actuator_extended = True
                    self.x_past = self.x
                
                if self.block == 1 and self.actuator_extended == True:
                    self.action = 2
                    
        







            rate.sleep()

if __name__ == '__main__':
    try:
        rc_listener = RCListener()
        rc_listener.start()
    except rospy.ROSInterruptException:
        pass
