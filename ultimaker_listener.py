#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import serial
import ultimaker_path_planning as upp

ser = serial.Serial()  # define class


def callback(data):  # logging user input data, defining path planning
    rospy.loginfo(rospy.get_caller_id())  # + "  I heard %s", data.data)
    print('I heard ' + data.data)
    
    if data.data == 'path_1':  # check user input against predefined path matching words
        upp.path_1()


def listener():
    rospy.init_node('ultimaker_listener', anonymous=True)
    rospy.Subscriber('ultimaker_chatter', String, callback)
    print('Hello there! I am listening')
    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped


if __name__ == '__main__':
    listener()
    # callback('run')
