#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from teamwork.msg import KeyData  # Import the custom message

import cv2 as cv
import numpy as np
import socket
import struct
import time

class RouterNode:
    def __init__(self):
        self.key_data_publisher = rospy.Publisher('/key_data', KeyData, queue_size=10)

        rospy.Subscriber('/camera/image', Image, self.image_callback)

        self.display_key = None

    def image_callback(self, image_msg):
        try:
            # Convert image message to OpenCV format
            cv_image = cv.imdecode(np.frombuffer(image_msg.data, dtype=np.uint8), cv.IMREAD_COLOR)

            server_ip = '192.168.0.100'  # Replace with the IP address of the receiving laptop
            server_port = 1234

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                server_socket.connect((server_ip, server_port))

                # Convert the frame to JPEG format
                data = cv.imencode('.jpg', cv_image)[1].tobytes()
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

                    time.sleep(0.1)

        except Exception as e:
            # Handle exceptions
            rospy.logerr(f"Error: {e}")

if __name__ == '__main__':
    try:
        rospy.init_node('router_node', anonymous=True)
        router_node = RouterNode()

        # While loop to keep the node alive until it is explicitly stopped
        while not rospy.is_shutdown():
            rospy.sleep(0.1)

    except rospy.ROSInterruptException:
        pass
