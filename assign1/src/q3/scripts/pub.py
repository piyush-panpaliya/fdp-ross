#!/usr/bin/python3

import rospy
from std_msgs.msg import Float32, Int32
import time

def publisher_node():
    rospy.init_node('publisher_node', anonymous=True)
    pub_float = rospy.Publisher('float_topic', Float32, queue_size=10)
    pub_int = rospy.Publisher('int_topic', Int32, queue_size=10)
    rate = rospy.Rate(1)  # Publish rate: 1 Hz

    while not rospy.is_shutdown():
        float_value = 3.14  # Sample float value
        int_value = 42      # Sample integer value

        pub_float.publish(float_value)
        pub_int.publish(int_value)

        rospy.loginfo("Published float value: %f, integer value: %d", float_value, int_value)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher_node()
    except rospy.ROSInterruptException:
        pass
