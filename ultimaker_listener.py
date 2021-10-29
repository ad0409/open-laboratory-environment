#!/usr/bin/env python3
# python3 -m serial.tools.list_ports

import rospy
from std_msgs.msg import String
import serial
import time


# def move_printer(x_mm):
#     raw_command = bytes('G0 X' +str(x_mm) +'F0\n')
#
#     return raw_command


def callback(data):
    rospy.loginfo(rospy.get_caller_id())  # + "  I heard %s", data.data)
    print('I heard ' + data.data)
    mydict = {'homing': 'G28\n',
              'run': 'do',
              'taille': 1.75}
    # print('Translating ' + data.data,  'to ' + mydict[data.data],)
    # encoded_user_input = mydict[data.data]
    # print('Encoded ' +mydict[data.data], 'to' + encoded_user_input)
    # homing = 'G28\n'  # better solution to encode string to bytes
    # ser.write(str.encode(mydict[data.data]))

    ser = serial.Serial()
    ser.port = '/dev/ttyACM0'
    ser.baudrate = 250000
    # ser.bytesize =
    ser.parity = serial.PARITY_EVEN
    ser.stopbits = serial.STOPBITS_ONE
    ser.timeout = 1
    ser.xonxoff = 0
    ser.rtscts = 1
    ser.dsrdtr = 1
    print('serial is open: ' + str(ser.is_open))

    print('serial is open: ' + str(ser.is_open))

    if ser.is_open:
        print('Serial open.. continue')
    else:
        print('Serial closed... open it.')

        ser.open()  # check ser.is_open to see if serial is open
        print('Wait 1s')
        time.sleep(1)

    print('Printer online')
    print('inline bytes waiting: ' + str(ser.in_waiting))

    print('Flushing Data')
    ser.flush()
    time.sleep(1)
    print('inline bytes waiting: ' + str(ser.in_waiting))

    print('Do some magic')
    print('Home:')
    ser.write(str.encode(mydict[data.data]))

    print('Wait 1s')
    time.sleep(1)
    print('Move X!')
    ser.write(bytes(b'G0 X100 F0\n'))
    # ser.write(bytes(b'G91'))
    # print('Move X!')
    # x_mm_wanted = 100
    # ser.write(move_printer(x_mm_wanted))

    print('Moving!')
    print('Call Read positions:')
    ser.write(bytes(b'M114\n'))
    print('Read serial:')
    print(ser.read())
    print('Move Y!')
    ser.write(bytes(b'G0 Y100.0 F0\n'))
    # ser.write(bytes(b'G90'))
    print('Sleep for 1s')
    time.sleep(1)
    print('Move -X!')
    ser.write(bytes(b'G0 X-100.0 F0\n'))
    print('Home again:')
    # ser.write(bytes(b'G28\n'))
    ser.write(str.encode(mydict[data.data]))

    print('Wake up')
    print('inline bytes waiting: ' + str(ser.in_waiting))
    # time.sleep(1)

    print('Sleep for 1s')
    time.sleep(1)
    print('inline bytes waiting: ' + str(ser.in_waiting))


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
