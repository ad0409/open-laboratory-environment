#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo(rospy.get_caller_id())  # + "  I heard %s", data.data)
    print('I heard ' + data.data)
    mydict = {'homing':'G28',
              'poids':70,
              'taille':1.75}
    print('Sending ' + mydict[data.data], 'to printer')


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('ultimaker_listener', anonymous=True)

    rospy.Subscriber('ultimaker_chatter', String, callback)
    print('Hello there! I am listening')

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
