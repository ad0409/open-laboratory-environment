#!/usr/bin/env python3
import serial
import time

ser = serial.Serial()  # define class


def move_printer_x(mm_wanted_x):  # linear moving X, currently not working with negative ints
    print('Linear moving X ' + mm_wanted_x, ' mm')
    raw_command_x = str.encode('G0 X ' + str(mm_wanted_x) + ' F0\n')
    return raw_command_x


def move_printer_y(mm_wanted_y):  # linear moving Y, currently not working with negative ints
    print('Linear moving Y ' + mm_wanted_y, ' mm')
    raw_command_y = str.encode('G0 X ' + str(mm_wanted_y) + ' F0\n')
    return raw_command_y


def move_printer_z(mm_wanted_z):  # linear moving Z, currently not working with negative ints
    print('Linear moving Z ' + mm_wanted_z, ' mm')
    raw_command_z = str.encode('G0 X ' + str(mm_wanted_z) + ' F0\n')
    return raw_command_z


def homing_printer():  # homing X,Y,Z
    print('Homing X,Y,Z')
    command_homing = str.encode('G28\n')
    return command_homing


def open_serial_port():
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

    if ser.is_open:
        print('Serial open... continue')
    else:
        print('Serial closed... open it.')
        ser.open()  # check ser.is_open to see if serial is open
        print('Wait 1s')
        time.sleep(1)


def close_serial_port():
    if ser.is_open:
        print('Serial open... closing now.')
        ser.close()  # check ser.is_open to see if serial is open
        print('Serial closed.')
        print('Wait 1s')
        time.sleep(1)
    else:
        print('Serial closed.')
