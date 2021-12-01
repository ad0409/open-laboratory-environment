#!/usr/bin/env python3
"""
Author: Adrian Falke
Email: <adrian.falke[at]gmail.com>
Credits: http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
"""

import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo("I heard %s", data.data)


def listener():
    rospy.init_node('ultimaker_listener_data_logger')
    rospy.Subscriber('data_logger', String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
