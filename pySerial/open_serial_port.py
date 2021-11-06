#!/usr/bin/env python3
import serial
import time
# import ultimaker_support_functions as usf

ser = serial.Serial()  # define class


def schedule_1():
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
    time.sleep(10)

    if ser.is_open:
        print('Serial open.. continue')
    else:
        print('Serial closed... open it.')

        ser.open()  # check ser.is_open to see if serial is open
        print('Wait 1s')
        time.sleep(8)

    print('Printer online')
    print('inline bytes waiting: ' + str(ser.in_waiting))
    # if ser.in_waiting == 0:
    #     ser.write(b'G28')
    #     time.sleep(0.1)

    print('Flushing Data')
    ser.flush()
    time.sleep(15)
    print('inline bytes waiting: ' + str(ser.in_waiting))
    print('Do some magic')
    print('Home:')
    ser.write(bytes(b'G28\n'))
    ser.write(bytes(b'M114\n'))

    time.sleep(15)
    print('Move X!')
    ser.write(bytes(b'G91\n'))
    ser.write(bytes(b'G0 X50.0 F0\n'))
    ser.write(bytes(b'G90\n'))
    ser.write(bytes(b'M114\n'))

    time.sleep(15)
    print('Move Y!')
    ser.write(bytes(b'G91\n'))
    ser.write(bytes(b'G0 Y-100.0 F0\n'))
    ser.write(bytes(b'G90\n'))
    ser.write(bytes(b'M114\n'))

    time.sleep(15)
    print('Move -X!')
    ser.write(bytes(b'G91\n'))
    ser.write(bytes(b'G0 X-100.0 F0\n'))
    ser.write(bytes(b'G90\n'))
    ser.write(bytes(b'M114\n'))

    time.sleep(15)
    print('Move -Y!')
    ser.write(bytes(b'G91\n'))
    ser.write(bytes(b'G0 Y10.0 F0\n'))
    ser.write(bytes(b'G90\n'))
    ser.write(bytes(b'M114\n'))

    time.sleep(15)
    print('Move X,Y!')
    ser.write(bytes(b'G0 X100.0 Y100.0 F0\n'))
    ser.write(bytes(b'M114\n'))

    time.sleep(15)
    print('Move Z!')
    ser.write(bytes(b'G91\n'))
    ser.write(bytes(b'G0 Z-50.0 F0\n'))
    ser.write(bytes(b'G90\n'))
    ser.write(bytes(b'M114\n'))

    time.sleep(15)
    print('Move -Z!')
    ser.write(bytes(b'G91\n'))
    ser.write(bytes(b'G0 Z25.0 F0\n'))
    ser.write(bytes(b'G90\n'))
    ser.write(bytes(b'M114\n'))

    time.sleep(15)
    print('Home:')
    ser.write(bytes(b'G28\n'))
    ser.write(bytes(b'M114\n'))

    print('Wake up')
    print('inline bytes waiting: ' + str(ser.in_waiting))
    # time.sleep(1)

    print('Sleep for 1s')
    time.sleep(1)
    print('inline bytes waiting: ' + str(ser.in_waiting))
    # ser.close()
    # print('closing port')
    #
    #
    # # if ser.in_waiting == 0:
    # #     for i in cmd:
    # #         ser.write(i.encode())
    # #         time.sleep(0.1)
