#!/usr/bin/python3

import rospy
from std_msgs.msg import Int32

def fibonacci_publisher():
    rospy.init_node('q2_pub', anonymous=True)
    rate = rospy.Rate(1)  # 1 Hz

    # Fibonacci sequence terms
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    while not rospy.is_shutdown():
        for term in fibonacci_sequence:
            pub.publish(term)
            rate.sleep()

try:
    pub= rospy.Publisher('/fib', Int32, queue_size=10)
    fibonacci_publisher()
except rospy.ROSInterruptException:
    pass
