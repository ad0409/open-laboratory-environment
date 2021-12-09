#!/usr/bin/env python3
"""
Author: Adrian Falke
Email: <adrian.falke[at]gmail.com>
Credits: http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
"""

import rospy
from std_msgs.msg import String
import ultimaker_schedule_planning as usp
import ultimaker_support_functions as usf


def callback(data):  # logg user input data, defining path planning
    rospy.loginfo(rospy.get_caller_id())
    print('I heard ' + data.data)
    command_list = data.data.split()  # convert data [str] to [list]

    if command_list[0] == 'T1':  # check user input against predefined schedule matching words
        usp.schedule_1(command_list[1])
    elif command_list[0] == 'T2':  # check user input against predefined schedule matching words
        usp.schedule_1(command_list[1])
    elif data.data == 'disable':
        usf.disable()
    elif data.data == 'off':
        usf.printer_off()
    else:
        print('Wrong schedule name.')


def listener():
    rospy.init_node('ultimaker_listener', anonymous=True)  # initialize listener node
    rospy.Subscriber('ultimaker_chatter', String, callback)  # subscribe to topic
    print('Hello there, I am listening!')
    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped


def data_logger():
    rospy.init_node('ultimaker_data_logger', anonymous=True)
    rospy.Subscriber('data_logger', String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
    data_logger()

# SNIPPETS
# tmp_array = [None] * len(data.data)
# tmp_array[0] = data.data[0:1]
# tmp_array[1] = int(data.data[3:4])
# if tmp_array[0] == 'T1 10':
#     usp.schedule_1(tmp_array[1])
# command_list[0] = data.data[0:1]
# command_list[1] = int(data.data[3:4])
# elif data.data == 's1':
#     usp.schedule_2()
# elif data.data == 's2':
#     usp.schedule_2()
