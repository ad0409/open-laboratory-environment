#!/usr/bin/env python3
import serial
import time
import ultimaker_support_functions as usf

ser = serial.Serial()  # define class


def path_1():
    usf.open_serial_port()  # open serial port
    print('Printer online')
    # print('inline bytes waiting: ' + str(ser.in_waiting))
    print('Flushing Data')
    ser.flush()  # flushing data
    time.sleep(1)

    mm_wanted_x = 100
    raw_command_x = usf.move_printer_x(mm_wanted_x)  # moving x-axis
    print('RAW Command: ' + raw_command_x)
    ser.write(raw_command_x)

    mm_wanted_y = 100
    raw_command_y = usf.move_printer_y(mm_wanted_y)  # moving y-axis
    print('RAW Command: ' + raw_command_y)
    ser.write(raw_command_y)

    # mm_wanted_z = 100
    # raw_command_z = usf.move_printer_z(mm_wanted_z)  # moving z-axis
    # print('RAW Command: ' + raw_command_z)
    # ser.write(raw_command_z)

    usf.homing_printer()  # homing printer
    usf.close_serial_port()  # close serial port

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
