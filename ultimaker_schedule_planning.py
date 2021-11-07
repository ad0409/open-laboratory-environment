#!/usr/bin/env python3
"""
Author: Adrian Falke
Email: <adrian.falke[at]gmail.com>
"""

import serial
import time
import ultimaker_support_functions as usf

ser = serial.Serial()  # define class


def schedule_1():
    if ser.is_open:  # initialize serial port
        print('Serial open.. continue')
    else:
        print('Serial closed... open it.')
        ser.port = '/dev/ttyACM0'
        ser.baudrate = 250000
        # ser.bytesize =
        ser.parity = serial.PARITY_EVEN
        ser.stopbits = serial.STOPBITS_ONE
        ser.timeout = 1
        ser.xonxoff = 0
        ser.rtscts = 1
        ser.dsrdtr = 1
        ser.open()  # check ser.is_open to see if serial is open

    print('Flushing Data')
    ser.flush()

    time.sleep(6)
    ser.write(usf.homing_printer())  # home X,Y,Z

    time.sleep(6)
    mm_wanted_x = '50'  # move x-axis
    v_wanted_x = '1500'  # set feedrate
    ser.write(bytes(b'G91\n'))
    ser.write(usf.move_printer_x(mm_wanted_x, v_wanted_x))
    ser.write(bytes(b'G90\n'))
    ser.write(bytes(b'M114\n'))

    time.sleep(6)
    mm_wanted_y = '-50'  # move y-axis
    v_wanted_y = '2500'  # set feedrate
    ser.write(bytes(b'G91\n'))
    ser.write(usf.move_printer_y(mm_wanted_y, v_wanted_y))
    ser.write(bytes(b'G90\n'))
    ser.write(bytes(b'M114\n'))

    time.sleep(6)
    mm_wanted_z = '-50'  # move z-axis
    v_wanted_z = '2000'  # set feedrate
    ser.write(bytes(b'G91\n'))
    ser.write(usf.move_printer_z(mm_wanted_z, v_wanted_z))
    ser.write(bytes(b'G90\n'))
    ser.write(bytes(b'M114\n'))

    # time.sleep(4)
    # ser.write(bytes(b'G91\n'))
    # ser.write(usf.move_printer_x_y_center())
    # ser.write(bytes(b'G90\n'))
    # ser.write(bytes(b'M114\n'))

    time.sleep(6)
    ser.write(usf.homing_printer())  # home X,Y,Z

    time.sleep(4)
    usf.disable()  # disable steppers


def schedule_2():
    if ser.is_open:  # initialize serial port
        print('Serial open.. continue')
    else:
        print('Serial closed... open it.')
        ser.port = '/dev/ttyACM0'
        ser.baudrate = 250000
        # ser.bytesize =
        ser.parity = serial.PARITY_EVEN
        ser.stopbits = serial.STOPBITS_ONE
        ser.timeout = 1
        ser.xonxoff = 0
        ser.rtscts = 1
        ser.dsrdtr = 1
        ser.open()  # check ser.is_open to see if serial is open

    print('Flushing Data')
    ser.flush()

    time.sleep(6)
    ser.write(usf.homing_printer())  # home X,Y,Z

    time.sleep(6)
    mm_wanted_x = '50'  # move x-axis
    v_wanted_x = '1500'  # set feedrate
    ser.write(bytes(b'G91\n'))
    ser.write(usf.move_printer_x(mm_wanted_x, v_wanted_x))
    ser.write(bytes(b'G90\n'))
    ser.write(bytes(b'M114\n'))

    # time.sleep(6)
    # mm_wanted_y = '-50'  # move y-axis
    # v_wanted_y = '2500'  # set feedrate
    # ser.write(bytes(b'G91\n'))
    # ser.write(usf.move_printer_y(mm_wanted_y, v_wanted_y))
    # ser.write(bytes(b'G90\n'))
    # ser.write(bytes(b'M114\n'))
    #
    # time.sleep(6)
    # mm_wanted_z = '-50'  # move z-axis
    # v_wanted_z = '2000'  # set feedrate
    # ser.write(bytes(b'G91\n'))
    # ser.write(usf.move_printer_z(mm_wanted_z, v_wanted_z))
    # ser.write(bytes(b'G90\n'))
    # ser.write(bytes(b'M114\n'))

    # time.sleep(4)
    # ser.write(bytes(b'G91\n'))
    # ser.write(usf.move_printer_x_y_center())
    # ser.write(bytes(b'G90\n'))
    # ser.write(bytes(b'M114\n'))

    time.sleep(6)
    ser.write(usf.homing_printer())  # home X,Y,Z

    time.sleep(4)
    usf.disable()  # disable steppers

# SNIPPETS
# python3 -m serial.tools.list_ports
# homing = 'G28\n'  # better solution to encode string to bytes
# ser.write(str.encode(my_dict[data.data]))
# raw_command = move_printer(bytes([mm_wanted_x]))
# raw_command = move_printer(mm_wanted_x.to_bytes(2, byteorder='little'))
# print('inline bytes waiting: ' + str(ser.in_waiting))
# print('Do some magic')
# print('Home:')
# ser.write(str.encode(my_dict[data.data]))
# print('Wait 1s')
# time.sleep(1)
# print('Move X!')
# ser.write(bytes(b'G0 X100 F0\n'))
# ser.write(bytes(b'G91'))
# print('Move X!')
# print(move_printer(bytes(mm_wanted_x)))
# ser.write(str.encode(my_dict[data.data]))
# print('Moving!')
# print('Call Read positions:')
# ser.write(bytes(b'M114\n'))
# print('Read serial:')
# print(ser.read())
# print('Move Y!')
# ser.write(bytes(b'G0 Y100.0 F0\n'))
# # ser.write(bytes(b'G90'))
# print('Sleep for 1s')
# time.sleep(1)
# print('Move -X!')
# ser.write(bytes(b'G0 X-100.0 F0\n'))
# print('Home again:')
# # ser.write(bytes(b'G28\n'))
# ser.write(str.encode(my_dict[data.data]))
# print('Wake up')
# print('inline bytes waiting: ' + str(ser.in_waiting))
# time.sleep(1)
# print('Sleep for 1s')
# time.sleep(1)
# print('inline bytes waiting: ' + str(ser.in_waiting))
# raw_command = str.encode('G0 X 100 ' + 'F0\n')
# my_dict = {'homing': 'G28\n',
#            'run': 'do',
#            'taille': 1.75}
# usf.homing_printer()  # homing printer
# print('serial is open: ' + str(ser.is_open))
# usf.open_serial_port()  # open serial port
# print('Printer online')
# print('inline bytes waiting: ' + str(ser.in_waiting))

# time.sleep(8)
# ser.write(b'G2 I20 J20\n') # Move in a complete clockwise circle with the center offset
# time.sleep(6) # from the current position by [20, 20]
# ser.write(b'G2 I-20 J20\n')
# time.sleep(6)
# ser.write(b'G2 I-20 J-20\n')
# time.sleep(6)
# ser.write(b'G2 I20 J-20\n')
