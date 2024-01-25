#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import Image
from std_msgs.msg import UInt8
import cv2 as cv
from cv2 import aruco
import numpy as np
from cv_bridge import CvBridge, CvBridgeError

class ArucoDetector:
    def __init__(self):
        try:
            rospy.init_node('aruco_detector_node', anonymous=False)
            self.image_pub = rospy.Publisher("/camera/image", Image, queue_size=10)
            self.pose_pub = rospy.Publisher("/aruco/pose", PoseStamped, queue_size=10)
            self.block_pub = rospy.Publisher("/aruco/block", UInt8, queue_size=10)
            rospy.Subscriber("/mavros/rc/action", UInt8, self.action_callback)
            rospy.Subscriber("/mavros/rc/mode", UInt8, self.mode_callback)
            self.rate = rospy.Rate(30)

            calib_data_path = "/home/jetson/Desktop/calib_data/MultiMatrix.npz"
            calib_data = np.load(calib_data_path)

            self.cam_mat = calib_data["camMatrix"]
            self.dist_coef = calib_data["distCoef"]
            self.marker_size = 8  # centimeters (measure your printed marker size)
            self.marker_dict = cv.aruco.getPredefinedDictionary(aruco.DICT_5X5_250)
            self.param_markers = cv.aruco.DetectorParameters()
            self.blockage_threshold = 1
            self.blocked = 0
            self.marker_detected = False
            self.actuator_extended = False
            self.action = 0
            self.mode = 1
            self.mode_status = "Full Manual"
            self.cap = cv.VideoCapture(0)
            self.bridge = CvBridge()
        except Exception as e:
            rospy.logerr("Error in camera: {}".format(str(e)))
        

    def calculate_blockage_percentage(self, frame):
    # Convert the frame to grayscale
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Apply a threshold to create a binary mask
        _, thresholded = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)

        # Calculate the percentage of white pixels in the mask
        total_pixels = frame.shape[0] * frame.shape[1]
        white_pixels = np.sum(thresholded == 255)
        blockage_percentage = (white_pixels / total_pixels) * 100

        return blockage_percentage
    

    def action_callback(self, data):
        self.action = data.data
    

    def mode_callback(self, data):
        self.mode = data.data

    def calculate_yaw_angle(self, rMat):
        # Extract yaw angle from rotation matrix
        yaw_rad = np.arctan2(rMat[1, 0], rMat[0, 0])
        return np.degrees(yaw_rad)
    
    def publish_pose(self, center_x, center_y, distance, marker_id, rMat):
        pose_msg = PoseStamped()
        pose_msg.header.stamp = rospy.Time.now()
        pose_msg.pose.position.x = center_x
        pose_msg.pose.position.y = center_y
        pose_msg.pose.position.z = distance
        pose_msg.pose.orientation.z = self.calculate_yaw_angle(rMat)
        pose_msg.pose.orientation.w = marker_id
        self.pose_pub.publish(pose_msg)

    def publish_image(self, frame):
        try:
            image_message = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            self.image_pub.publish(image_message)
        except CvBridgeError as e:
            rospy.logerr("Error publishing image: {}".format(str(e)))

    def publish_block_status(self, blocked):
        block_msg = UInt8()
        block_msg.data = blocked
        self.block_pub.publish(block_msg)

    def start(self):
            while not rospy.is_shutdown():
                ret, frame = self.cap.read()

                # Calculate blockage percentage
                blockage_percentage = self.calculate_blockage_percentage(frame)
                if blockage_percentage <= self.blockage_threshold:
                    self.blocked = 1
                else:
                    self.blocked = 0

                self.publish_block_status(self.blocked)

                gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                marker_corners, marker_IDs, reject = aruco.detectMarkers(
                    gray_frame, self.marker_dict, parameters=self.param_markers
                )
                if marker_corners:
                    rVec, tVec, _ = aruco.estimatePoseSingleMarkers(
                        marker_corners, self.marker_size, self.cam_mat, self.dist_coef
                    )
                    self.marker_detected = True

                    total_markers = range(0, marker_IDs.size)
                    for ids, corners, i in zip(marker_IDs, marker_corners, total_markers):
                        cv.polylines(
                            frame, [corners.astype(np.int32)], True, (0, 255, 255), 4, cv.LINE_AA
                        )
                        corners = corners.reshape(4, 2)
                        corners = corners.astype(int)
                        top_right = corners[0].ravel()
                        top_left = corners[1].ravel()
                        bottom_right = corners[2].ravel()
                        bottom_left = corners[3].ravel()

                        # Calculating the distance
                        distance = np.sqrt(
                            tVec[i][0][2] ** 2 + tVec[i][0][0] ** 2 + tVec[i][0][1] ** 2
                        )
                        # Draw the pose of the marker
                        point = cv.drawFrameAxes(frame, self.cam_mat, self.dist_coef, rVec[i], tVec[i], 4, 4)

                        center_x = int(np.mean(corners[:, 0]))
                        center_y = int(np.mean(corners[:, 1]))

                        # Draw a circle at the center of the marker
                        cv.circle(frame, (center_x, center_y), radius=5, color=(0, 255, 0), thickness=-1)


                        cv.putText(
                            frame,
                            f"id: {ids[0]} Dist: {round(distance, 2)}",
                            top_right,
                            cv.FONT_HERSHEY_PLAIN,
                            1.3,
                            (0, 0, 255),
                            2,
                            cv.LINE_AA,
                        )
                        cv.putText(
                            frame,
                            f"x:{round(tVec[i][0][0],1)} y: {round(tVec[i][0][1],1)} ",
                            bottom_right,
                            cv.FONT_HERSHEY_PLAIN,
                            1.0,
                            (0, 0, 255),
                            2,
                            cv.LINE_AA,
                        )

                        # Draw the centering
                        H, W, _ = frame.shape
                        # calculate the center of the frame
                        centerX = W // 2
                        centerY = H // 2

                        # draw a circle in the center of the frame
                        cv.circle(frame, center=(centerX, centerY), radius=5, color=(0,0,255), thickness=-1)
                        
                        # draw arrow
                        cv.arrowedLine(frame, (centerX, centerY), (center_x, center_y), color=(0, 255, 0), thickness=2)

                        rMat, _ = cv.Rodrigues(rVec[i])

                        self.publish_pose(center_x, center_y, distance, ids[0], rMat)

                else:
                    self.marker_detected = False

                if self.mode == 1:
                    self.mode_status = "Full Manual"
                elif self.mode == 2:
                    self.mode_status = "Assisted Manual"
                elif self.mode == 3:
                    self.mode_status = "Full Auto"

                if self.action == 1:
                    self.actuator_extended = True
                elif self.action == 2:
                    self.actuator_extended = False

                if self.action == 0:
                    self.magnet_on = False
                else:
                    self.magnet_on = True

                status_text = f"Actuator Extended: {self.actuator_extended}, Magnet On: {self.magnet_on}"
                mode_text = f"Mode: {self.mode_status}, Blocked?: {self.blocked}"

                cv.putText(frame, status_text, (10, 30), cv.FONT_HERSHEY_PLAIN, 1.0, (0, 255, 0), 2, cv.LINE_AA)
                cv.putText(frame, mode_text, (10, 60), cv.FONT_HERSHEY_PLAIN, 1.0, (0, 255, 0), 2, cv.LINE_AA)

                self.publish_image(frame)  # Publish the image

                self.frame = frame

                self.rate.sleep()



if __name__ == '__main__':
    try:
        aruco_detector = ArucoDetector()
        aruco_detector.start()
    except rospy.ROSInterruptException:
        pass
    except Exception as e:
        rospy.logerr("Error in main: {}".format(str(e)))
