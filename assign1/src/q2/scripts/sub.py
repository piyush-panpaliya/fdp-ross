#!/usr/bin/python3

import rospy
from std_msgs.msg import Int32

def sub():
    rospy.init_node('q2_sub', anonymous=True)
    rospy.Subscriber('/fib', Int32, fibonacci_callback)

    rospy.spin()

def fibonacci_callback(data):
    term = data.data
    fibonacci_sequence = generate_fibonacci(term)
    for fib_term in fibonacci_sequence:
        pub.publish(fib_term)

def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

try:
    pub = rospy.Publisher('/fib1', Int32, queue_size=10)
    sub()
except rospy.ROSInterruptException:
    pass
