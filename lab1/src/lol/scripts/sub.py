#!/usr/bin/python3
import rospy
from std_msgs.msg import String

def callback(msg):
    data = msg.data
    print("data is %s"% data)

if __name__ == "__main__":
    rospy.init_node('nodeSUB',anonymous=True)
    rospy.Subscriber('vartalap',String,callback)
    rospy.spin()