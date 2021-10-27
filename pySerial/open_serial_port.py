#!/usr/bin/env python3

#example1               # for more info visit https://pythonhosted.org/pyserial/shortintro.html#opening-serial-ports
import serial

ser = serial.Serial('/dev/ttyUSB0', 250000)  # open serial port at 250000
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()             # close port



# example 2
import serial

ser = serial.Serial()
ser.baudrate = 19200
ser.port = 'COM1'
ser
Serial<id=0xa81c10, open=False>(port='COM1', baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)
ser.open()
ser.is_open
True
ser.close()
ser.is_open
False
