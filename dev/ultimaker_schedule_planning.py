#!/usr/bin/env python3
import serial
import time
import ultimaker_support_functions as usf

ser = serial.Serial()  # define class


def schedule_1():
    if ser.is_open:
        print('Serial open... continue')
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
        ser.flush()  # flushing data

    time.sleep(1)
    print('Flushing Data')
    ser.flush()  # flushing data
    time.sleep(1)

    mm_wanted_x = '100'  # moving x-axis
    ser.write(usf.move_printer_x(mm_wanted_x))
    ser.flush()  # flushing data
    time.sleep(1)
    mm_wanted_x = '-100'  # moving x-axis
    ser.write(usf.move_printer_x(mm_wanted_x))
    #
    # mm_wanted_x = '-20'  # moving x-axis
    # ser.write(usf.move_printer_x(mm_wanted_x))

    ser.flush()  # flushing data
    time.sleep(1)
    # command_enable = str.encode('M17\n')
    # print(command_enable)
    # ser.write(command_enable)

    mm_wanted_y = '100'  # moving y-axis
    ser.write(usf.move_printer_y(mm_wanted_y))
    ser.flush()  # flushing data
    time.sleep(1)
    mm_wanted_y = '-100'  # moving y-axis
    ser.write(usf.move_printer_y(mm_wanted_y))
    # command_y = str.encode('G0 X100.0 1500 F0\n')
    # print(command_y)
    # ser.write(command_y)

    # ser.flush()  # flushing data
    # command_d = str.encode('G0 Y100.0 1000 F0\n')
    # print(command_d)
    # ser.write(command_d)

    # ser.flush()  # flushing data
    # time.sleep(1)
    # mm_wanted_z = '20'  # moving z-axis
    # ser.write(usf.move_printer_z(mm_wanted_z))

    # ser.flush()  # flushing data
    # time.sleep(1)
    # ser.write(usf.homing_printer())  # ser.write() method must be invoked in usp.py file.
    # usf.stop()  # It otherwise causes trouble passing arguments across files

    # time.sleep(1)
    # usf.move_printer_x_y_center()
    # ser.write(usf.move_printer_x_y_center())
    # G0 X100.0 Y100 .0 F0

    ser.flush()  # flushing data
    time.sleep(1)
    ser.write(usf.homing_printer())  # ser.write() method must be invoked in usp.py file.
    usf.stop()  # It otherwise causes trouble passing arguments across files
    time.sleep(3)
    usf.stop()

    # ser.close()  # close serial port
    # usf.close_serial_port()  # close serial port

# def schedule_2():


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
