#!/usr/bin/python3

import rospy
from std_msgs.msg import Int32

def sub():
    rospy.init_node('q1_sub', anonymous=True)
    rospy.Subscriber('/num1', Int32, num1_callback)
    rospy.Subscriber('/num2', Int32, num2_callback)

    rospy.spin()

def num1_callback(data):
    global num1
    num1 = data.data
    calculate_sum()

def num2_callback(data):
    global num2
    num2 = data.data
    calculate_sum()

def calculate_sum():
    global num1, num2
    result = num1 + num2
    sum_pub.publish(result)

try:
    num1 = 0
    num2 = 0
    sum_pub = rospy.Publisher('/sum', Int32, queue_size=10)
    sub()
except rospy.ROSInterruptException:
    pass
