#!/usr/bin/env python3

import rospy
from std_msgs.msg import UInt8
import Jetson.GPIO as GPIO
import threading


class ActionListener:
    def __init__(self):
        rospy.init_node('actuator_control_node', anonymous=False)
        rospy.Subscriber("/mavros/rc/action", UInt8, self.action_callback)
        self.rate = rospy.Rate(10) 
        self.action = 0
        self.motor1Pin1 = 37
        self.motor1Pin2 = 35
        self.motor2Pin1 = 15
        self.motor2Pin2 = 19
        self.extended = False


        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.motor1Pin1, GPIO.OUT)
        GPIO.setup(self.motor1Pin2, GPIO.OUT)
        GPIO.setup(self.motor2Pin1, GPIO.OUT)
        GPIO.setup(self.motor2Pin2, GPIO.OUT)



    def action_callback(self, data):
        self.action = data.data

    def start(self):
        while not rospy.is_shutdown():
            #rospy.loginfo("Current action: {}".format(self.action))
            if self.action == 0:
                self.magnet_Off()
            elif self.action == 1 and self.extended == False:
                self.extend()
                rospy.loginfo("Extend")
                self.extended = True
            elif self.action == 2 and self.extended == True:
                self.retract()
                rospy.loginfo("Retract")
                self.extended = False


            self.rate.sleep()

    def motor1_backward(self):
            GPIO.output(self.motor1Pin1, False)
            GPIO.output(self.motor1Pin2, True)

    def motor1_forward(self):
        GPIO.output(self.motor1Pin1, True)
        GPIO.output(self.motor1Pin2, False)

    def motor1_stop(self):
        GPIO.output(self.motor1Pin1, False)
        GPIO.output(self.motor1Pin2, False)

    def motor2_backward(self):
        GPIO.output(self.motor2Pin1, False)
        GPIO.output(self.motor2Pin2, True)


    def motor2_forward(self):
        GPIO.output(self.motor2Pin1, True)
        GPIO.output(self.motor2Pin2, False)


    def magnet_Off(self):

        GPIO.output(self.motor1Pin1, False)
        GPIO.output(self.motor1Pin2, False)
        GPIO.output(self.motor2Pin1, False)
        GPIO.output(self.motor2Pin2, False)

    def extend(self):
        thread1 = threading.Thread(target=self.motor1_forward)
        thread2 = threading.Thread(target=self.motor2_forward)
        thread1.daemon = True
        thread2.daemon = True
        # Start both threads
        thread1.start()
        thread2.start()




    def retract(self):
        # Create two threads to run motor1_backward and motor2_backward simultaneously



        thread1 = threading.Thread(target=self.motor1_backward)
        thread2 = threading.Thread(target=self.motor2_backward)
        thread1.daemon = True
        thread2.daemon = True
        # Start both threads
        thread1.start()
        #time.sleep(0.1)
        timer1 = threading.Timer(0.1, thread2.start)
        timer1.start()
        #thread2.start()
        #time.sleep(2)
        timer2 = threading.Timer(2.1, self.motor1_stop)
        timer2.start()
        #self.motor1_stop()
        #time.sleep(1)
        timer3 = threading.Timer(3.1, self.motor1_backward)    
        timer3.start()    
        #self.motor1_backward(0)
        #time.sleep(0.5)


if __name__ == '__main__':
    try:
        action_listener = ActionListener()
        action_listener.start()
    except rospy.ROSInterruptException:
        pass
    except Exception as e:
        rospy.logerr("Error in main: {}".format(str(e)))
