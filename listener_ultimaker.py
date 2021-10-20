#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "  I heard %s", data.data)
#     print(data.data)
#     if data.data == 'on':
        # Turn the LED on and wait for 0.5 seconds
        # print('led on')
#     elif data.data == 'off':
        # Turn the LED off and wait for 0.5 seconds
        # print('led off')
#     else:
#         print('invalid input')


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener_ultimaker', anonymous=True)

    rospy.Subscriber('chatter_ultimaker', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
