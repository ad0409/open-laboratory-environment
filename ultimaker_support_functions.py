#!/usr/bin/env python3
"""
Author: Adrian Falke
Email: <adrian.falke[at]gmail.com>
"""

import serial
import time
import serial.tools.list_ports

ser = serial.Serial()  # define class


def move_printer_x(mm_wanted_x, v_wanted_x):  # linear moving X
    print('Linear moving X=' + mm_wanted_x + '[mm] ' + 'with Feedrate=' + v_wanted_x + '[mm/min]')
    raw_command_x = str.encode('F' + str(v_wanted_x) + ' G0 X ' + str(mm_wanted_x) + '\n')
    return raw_command_x


def move_printer_y(mm_wanted_y, v_wanted_y):  # linear moving Y
    print('Linear moving Y=' + mm_wanted_y + '[mm] ' + 'with Feedrate=' + v_wanted_y + '[mm/min]')
    raw_command_y = str.encode('F' + str(v_wanted_y) + ' G0 Y ' + str(mm_wanted_y) + '\n')
    return raw_command_y


def move_printer_z(mm_wanted_z, v_wanted_z):  # linear moving Z
    print('Linear moving Z=' + mm_wanted_z + '[mm] ' + 'with Feedrate=' + v_wanted_z + '[mm/min]')
    raw_command_z = str.encode('F' + str(v_wanted_z) + ' G0 Z ' + str(mm_wanted_z) + '\n')
    return raw_command_z


def homing_printer():  # home X,Y,Z
    print('Homing X,Y,Z')
    command_homing = str.encode('G28\n')
    return command_homing
    # return ser.write(command_homing)


def disable():  # disable steppers
    port_list = get_port()  # get list of available ports
    port_available = port_list.device  # get device name out of port list, cast into str
    if ser.is_open:  # initialize serial port
        print('Serial open.. continue')
    else:
        print('Serial closed... open it.')
        # ser.port = '/dev/ttyACM0'
        ser.port = port_available  # set available port
        ser.baudrate = 250000
        # ser.bytesize =
        ser.parity = serial.PARITY_EVEN
        ser.stopbits = serial.STOPBITS_ONE
        ser.timeout = 1
        ser.xonxoff = 0
        ser.rtscts = 1
        ser.dsrdtr = 1
        ser.open()  # check ser.is_open to see if serial is open

    ser.flush()  # flush data
    time.sleep(1)
    print('Disable steppers')
    command_disable = str.encode('M84\n')  # M84 = disable steppers
    ser.write(command_disable)
    time.sleep(3)
    command_disable = str.encode('M84\n')  # M84 = disable steppers
    ser.write(command_disable)


def printer_off():
    if ser.is_open:
        print('Serial already closed.')
    else:
        print('Serial open... close it now.')
        ser.close()


def get_port():  # auto check available ports
    ports = list(serial.tools.list_ports.comports())
    return ports[0]


def set_light(brightness_wanted):  # set LED brightness level
    print('Setting brightness level to ' + brightness_wanted)
    raw_command_brightness = str.encode('M42 S' + str(brightness_wanted) + '\n')
    time.sleep(0.1)
    return raw_command_brightness

# def move_printer_x_y_center():  # center X,Y
#     print('Centering X,Y with Feedrate=2500[mm/min]')
#     command_x_y_centering = str.encode('F2500 G0 X100.0 Y-100.0 \n')
#     return command_x_y_centering


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


# def printer_on():
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
#         ser.open()  # check ser.is_open to see if serial is open
#         ser.flush()  # flushing data
#         # time.sleep(10)
#     print('Printer ready.')

# SNIPPETS
# ports = serial.tools.list_ports.comports()
# print('This is ports[0]:')
# print(ports[0])
# port_name = ''.join(ports[0])
# port_name = port_name.strip(' Utimaker 2.0USB VID:PID=2341:0010 LOCATION=1-3:1.0')
# port_name1 = port_name.replace('LOCATION=1-3:1.0', '')
# print('This is port_name1:')
# print(port_name1)
# return port_name
# print(ports[0])
