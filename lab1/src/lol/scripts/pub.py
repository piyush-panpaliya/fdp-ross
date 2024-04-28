#!/usr/bin/python3
import rospy
from std_msgs.msg import String

def function():
    rospy.init_node('nodePUB' , anonymous=True)
    pub_float =rospy.Publisher('vartalap' , String, queue_size=10)
    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        s= String()
        s.data="okbhai"
        pub_float.publish(s)
        rate.sleep()

if __name__=="__main__":
    function()