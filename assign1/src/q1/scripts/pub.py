#!/usr/bin/python3

import rospy
from std_msgs.msg import Int32

def pub():
    rospy.init_node('q1_pub', anonymous=True)
    pub_num1 = rospy.Publisher('/num1', Int32, queue_size=10)
    pub_num2 = rospy.Publisher('/num2', Int32, queue_size=10)
    rate = rospy.Rate(1)  

    num1 = 5
    num2 = 7

    while not rospy.is_shutdown():
        print(1)
        pub_num1.publish(num1)
        pub_num2.publish(num2)
        rate.sleep()

try:
    pub()
except rospy.ROSInterruptException:
    pass

