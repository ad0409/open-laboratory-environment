#!/usr/bin/env python3           # this code works proper for commanding X,Y,Z individually
            
import serial                    # for more info visit https://pythonhosted.org/pyserial/shortintro.html#opening-serial-ports
import time

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

if ser.is_open:
    print('Serial open.. continue')
else:
    print('Serial closed... open it.')

    ser.open()  # check ser.is_open to see if serial is open
    print('Wait 1s')
    time.sleep(1)

print('Printer online')
print('inline bytes waiting: ' + str(ser.in_waiting))
# if ser.in_waiting == 0:
#     ser.write(b'G28')
#     time.sleep(0.1)
#
# time.sleep(1)
print('Flushing Data')
ser.flush()
time.sleep(1)
print('inline bytes waiting: ' + str(ser.in_waiting))

print('Do some magic')
print('Home:')
ser.write(bytes(b'G28\n'))
print('Wait 1s')
time.sleep(1)
# ser.write(bytes(b'G91'))
print('Move X!')
ser.write(bytes(b'G0 X100.0 F0\n'))
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
