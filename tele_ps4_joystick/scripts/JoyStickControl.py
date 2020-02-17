#!/usr/bin/python3
# Author: Don Thomas
# Description: This is the node written to control the robot based on ps4 joystick inputs

import rospy

from geometry_msgs.msg import Twist
import math
import time
import numpy as np
import sys
from enum import Enum
import message_filters
from motor import *

from turn import *

def turnOffMotor():
    global motor_controller
    motor_controller.destroy() # Clearing RAM Space and GPIO Pin Setups

def motion(data):
    global motor_controller
    
    # Determines the gains for linear and steering based on user inputs from the ps4 controller 
    angular_degree = data.linear.y 
    linear_speed = data.linear.z

 
    # I had to make this equation for my version of robot version so you might have to change the equation for you
    # 370 aligned my steering at the middle 
    anglar_degree = 2*angular_degree*110+370  
        
    if 0<linear_speed:
        motor_controller.motor_left(1,0,abs(linear_speed*50))
        motor_controller.motor_right(1,0,abs(linear_speed*50))

    else:
        motor_controller.motor_left(1,1,abs(linear_speed*50))
        motor_controller.motor_right(1,1,abs(linear_speed*50))

    turn_ang(int(anglar_degree))

def listener():
    rospy.init_node("PiCar_Joystick", anonymous=True) # Node 
    rospy.on_shutdown(turnOffMotor) # Run this program when the program stops
    # Callback Method when joystick commands are recived 
    rospy.Subscriber("/cmd_vel", Twist, motion, queue_size=1)
    
    print('setup')
    rospy.spin()
    print('shuting down')


if __name__ == "__main__":
    # Motor controller object is created here
    motor_controller = MotorController() # Object creation for the motor controller class
    listener()
