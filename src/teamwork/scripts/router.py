#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from teamwork.msg import KeyData  # Import the custom message

import cv2 as cv
import numpy as np
import socket
import struct
from cv_bridge import CvBridge


class RouterNode:
    def __init__(self):
        rospy.init_node('router_node', anonymous=True)
        self.display_key = None
        self.cv_image = None
        self.rate = rospy.Rate(30)
        self.key_data_publisher = rospy.Publisher('/key_data', KeyData, queue_size=10)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/camera/image', Image, self.image_callback)


    def image_callback(self, image_msg):
        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(image_msg, desired_encoding="bgr8")
            

        except Exception as e:
            rospy.logerr("Error in image callback: {}".format(str(e)))

    def start(self):

        while not rospy.is_shutdown():
            
            try:
                server_ip = '192.168.0.100'  # Replace with the IP address of the receiving laptop
                server_port = 1234

                server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_socket.connect((server_ip, server_port))
                print("connected")
                

                while not rospy.is_shutdown():

                
                    # Convert the frame to JPEG format
                    data = cv.imencode('.jpg', self.cv_image)[1].tobytes()
                    message_size = struct.pack("I", len(data))

                    # Send the frame size
                    server_socket.sendall(message_size)

                    # Send the frame data
                    server_socket.sendall(data)

                    # Receive key data
                    key_data = server_socket.recv(1024)

                    if key_data:
                        received_key = struct.unpack("B", key_data)[0]

                        if received_key == 255:
                            received_key = None
                        else:
                            received_key = chr(received_key)

                        # Publish both router key and display key in a single message
                        key_msg = KeyData()
                        key_msg.router_key = received_key
                        key_msg.display_key = self.display_key

                        self.key_data_publisher.publish(key_msg)

                        if self.display_key is None and received_key is not None:
                            self.display_key = received_key
                        elif self.display_key is not None and received_key is None:
                            self.display_key = self.display_key
                        elif self.display_key is not None and received_key is not None:
                            if received_key != self.display_key:
                                self.display_key = received_key

                        self.rate.sleep()

            except Exception as e:
                rospy.logerr("Error in router: {}".format(str(e)))
            

if __name__ == '__main__':
    try:
        print("router started")
        router_node = RouterNode()
        router_node.start()


    except rospy.ROSInterruptException:
        pass

    except Exception as e:
        rospy.logerr("Error in main: {}".format(str(e)))

