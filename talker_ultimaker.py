
#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('chatter_ultimaker', String, queue_size=10)
    rospy.init_node('talker_ultimaker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        user_input = input("Enter Input: ").strip()
        if user_input == "done":
            print('finished')
            break
        rospy.loginfo(user_input)
        pub.publish(user_input)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
