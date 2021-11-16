#!/usr/bin/env python3
import serial
import time

ser = serial.Serial()  # define class


def printer_on():
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
        # time.sleep(10)


def printer_off():
    if ser.is_open:
        print('Serial already closed.')
    else:
        print('Serial open... close it now.')
        ser.close()


def move_printer_x(mm_wanted_x):  # linear moving X
    print('Linear moving X ' + mm_wanted_x, 'mm')
    raw_command_x = str.encode('G0 X ' + str(mm_wanted_x) + ' F0\n')
    return raw_command_x


def move_printer_y(mm_wanted_y):  # linear moving Y
    print('Linear moving Y ' + mm_wanted_y, 'mm')
    raw_command_y = str.encode('G0 Y' + str(mm_wanted_y) + ' F0\n')
    return raw_command_y


def move_printer_z(mm_wanted_z):  # linear moving Z
    print('Linear moving Z ' + mm_wanted_z, 'mm')
    raw_command_z = str.encode('G0 Z ' + str(mm_wanted_z) + 'F0\n')
    return raw_command_z


def move_printer_x_y_center():  # centering X,Y
    print('Centering X,Y')
    command_x_y_centering = str.encode('G0 X100.0 Y100.0 F0\n')
    return command_x_y_centering


def homing_printer():  # homing X,Y,Z
    print('Homing X,Y,Z')
    command_homing = str.encode('G28\n')
    return command_homing
    # return ser.write(command_homing)


def stop():
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
        print('Wait 1s')
    # usf.open_serial_port()  # open serial port
    # print('Printer online')
    # print('inline bytes waiting: ' + str(ser.in_waiting))
    print('Flushing Data')
    ser.flush()  # flushing data
    time.sleep(1)
    print('Disable steppers')
    command_disable = str.encode('M84\n')  # M84 = disable steppers
    ser.write(command_disable)
    # print('Serial closed.')
    # ser.close()

# def open_serial_port():
#     if ser.is_open:
#         print('Serial open... continue')
#     else:
#         print('Serial closed... open it.')
#         ser.port = '/dev/ttyACM0'
#         ser.baudrate = 250000
#         # ser.bytesize =
#         ser.parity = serial.PARITY_EVEN
#         ser.stopbits = serial.STOPBITS_ONE
#         ser.timeout = 1
#         ser.xonxoff = 0
#         ser.rtscts = 1
#         ser.dsrdtr = 1
#         # ser.open()  # check ser.is_open to see if serial is open
#         print('Wait 1s')


# def close_serial_port():
#     if ser.is_open:
#         print('Serial open... closing now.')
#         ser.close()  # check ser.is_open to see if serial is open
#         print('Serial closed.')
#         print('Wait 1s')
#         time.sleep(1)
#     else:
#         print('Serial closed.')
