#!/usr/bin/env python3
"""
Author: Adrian Falke
Email: <adrian.falke[at]gmail.com>
"""

import serial
import time
import ultimaker_support_functions as usf
import serial.tools.list_ports
import sys

if sys.version_info.major < 3:  # check if python version > 3 is used
    print("You need to run this on Python 3")
    sys.exit(-1)
ser = serial.Serial()  # define class


def schedule_1(command_list=5):

    """Initialize port"""
    port_list = usf.get_port()  # get list of available ports
    port_available = port_list.device  # get device name out of port list, cast into str
    if ser.is_open:  # check to see if serial is open
        ser.port = port_available  # set available port
        ser.baudrate = 250000
        # ser.bytesize =
        ser.parity = serial.PARITY_NONE
        ser.stopbits = serial.STOPBITS_ONE
        ser.timeout = 0
        ser.xonxoff = None
        ser.rtscts = None
        ser.dsrdtr = None
        print('Serial open... continue.')
    else:
        print('Serial closed... open it.')  # initialize serial port
        # ser.port = '/dev/ttyACM0'
        ser.port = port_available  # set available port
        ser.baudrate = 250000
        # ser.bytesize =
        ser.parity = serial.PARITY_NONE
        ser.stopbits = serial.STOPBITS_ONE
        ser.timeout = 0
        ser.xonxoff = None
        ser.rtscts = None
        ser.dsrdtr = None
        ser.open()  # open serial port
        time.sleep(7)  # give the printer time to initialize
        printer_handshake = ser.readall()
        printer_handshake_decoded = printer_handshake.decode('utf-8')
        print('PRINTER HANDSHAKE: ', printer_handshake_decoded)

    """Starting schedule with homing all axes"""
    brightness_wanted = '255'  # set LED brightness [0-255]
    ser.write(usf.set_light(brightness_wanted))
    ser.write(usf.homing_printer())  # home X,Y,Z
    time.sleep(2)

    ser.flushInput()  # flush input-line before reading out data
    time.sleep(0.5)
    ser.write(b'M105\n')
    time.sleep(0.1)  # give the printer time to receive data
    printer_feedback = ser.readall()
    usf.log_data(printer_feedback)

    brightness_wanted = '130'  # set LED brightness str[0-255]
    ser.write(usf.set_light(brightness_wanted))
    mm_wanted_y = '-50'  # move y-axis
    v_wanted_y = '2500'  # set feedrate
    ser.write(bytes(b'G91\n'))
    ser.write(usf.move_printer_y(mm_wanted_y, v_wanted_y))
    ser.write(bytes(b'G90\n'))
    operation_time_move_printer_y = round((abs(int(mm_wanted_y) / int(v_wanted_y)) * 60), 2)
    print('Moving ' + str(operation_time_move_printer_y) + ' seconds.')
    time.sleep(operation_time_move_printer_y)  # sleep required time until movement is done

    brightness_wanted = '190'  # set LED brightness str[0-255]
    ser.write(usf.set_light(brightness_wanted))
    mm_wanted_x = '75'  # move x-axis
    v_wanted_x = '2000'  # set feedrate
    ser.write(bytes(b'G91\n'))
    ser.write(usf.move_printer_x(mm_wanted_x, v_wanted_x))
    ser.write(bytes(b'G90\n'))
    operation_time_move_printer_x = round((abs(int(mm_wanted_x) / int(v_wanted_x)) * 60), 2)
    print('Moving ' + str(operation_time_move_printer_x) + ' seconds.')
    time.sleep(operation_time_move_printer_x)  # sleep required time until movement is done

    print('Treatment time: ' + str(command_list) + ' seconds')
    time.sleep(int(command_list))

    brightness_wanted = '99'  # set LED brightness str[0-255]
    ser.write(usf.set_light(brightness_wanted))
    mm_wanted_z = '-25'  # move z-axis
    v_wanted_z = '2000'  # set feedrate
    ser.write(bytes(b'G91\n'))
    ser.write(usf.move_printer_z(mm_wanted_z, v_wanted_z))
    ser.write(bytes(b'G90\n'))
    operation_time_move_printer_z = round((abs(int(mm_wanted_z) / int(v_wanted_z)) * 60), 2)
    print('Moving ' + str(operation_time_move_printer_z) + ' seconds.')
    time.sleep(operation_time_move_printer_z)  # sleep required time until movement is done

    ser.flushInput()  # flush input-line before reading out data
    time.sleep(0.5)
    ser.write(bytes(b'M105\n'))
    time.sleep(0.1)  # give the printer time to receive data
    printer_feedback = ser.readall()
    usf.log_data(printer_feedback)

    brightness_wanted = '255'  # set LED brightness [0-255]
    ser.write(usf.set_light(brightness_wanted))
    ser.write(usf.homing_printer())  # home X,Y,Z

    time.sleep(4)
    usf.disable()  # disable steppers
    ser.flush()  # flush input-line before reading out data
    print(f"Waiting for the next job to do.")

# schedule_1()  # for debugging
# usf.disable()  # for debugging


def schedule_2():
    """
    Insert desired schedule here.
    """
