#  --------------------------------------------------------------
#  SNIPPETS
#  --------------------------------------------------------------

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
# ports = list(serial.tools.list_ports.comports())
# for p in ports:

# short = usf.get_port()
# sw = short.device
# port_name = short.strip(' - Ultimaker 2.0')
# string = usf.get_port()
# port_name = string.strip(' - Ultimaker 2.0')
# print(string)

# duty = 0.0
# try:
#     while 1:
#         while duty < 1.0:
#             ser.write(bytes(b'M42 S0\n'))
#             led.write(duty)
#             duty += 0.05
#             time.sleep(0.1)
#         while duty > 0.0:
#             led.write(duty)
#             duty -= 0.05
#             time.sleep(0.1)
# except KeyboardInterrupt:
#     pass
# ser.reset_input_buffer()
# ser.reset_output_buffer()
# ser.write(bytes(b'M105\n'))
# ser_bytes = ser.readline()
# print(ser_bytes)
# a = codecs.decode(ser_bytes, "ISO-8859-1").decode(ser_bytes, "UTF-8")
# print(a)
# decoded_bytes = float(ser_bytes[0:len(ser_bytes) - 2].decode("ascii"))
# print(decoded_bytes)

# b = ser.read_until(terminator='\n')
# a = ser.readlines()
# print(a)
# time.sleep(3)
# b = a.decode('utf-8')
# a = ser.read_until(terminator='\n')
# print(b)
# # print(port_chosen)
# print('Enter your commands below.\r\nInsert "exit" to leave the application.')
# # get keyboard input
# user_in = input()
# if input == 'exit':
#     ser.close()
#     exit()
# else:
#     # send the character to the device
#     # (note that I append a \r\n carriage return and line feed to the characters - this is requested by my device)
#     ser.write(str.encode(user_in + '\n'))
#     out = ''
#     # let's wait one second before reading output (let's give device time to answer)
#     time.sleep(1)
#     while True:
#         bytes_to_read = ser.in_waiting
#         ser.read(bytes_to_read)
#         # while ser.inWaiting() > 0:
#         #     # b"abcde".decode("utf-8")
#         #     data = ser.read_until()
#         #     # out = data.decode('utf-8')
#         #     out = data.decode('latin-1')
#         if bytes_to_read != '':
#             print('>>' + out)
#
# print('Flushing Data')
# ser.flush()
# time.sleep(7)
# ser.write(bytes(b'M105\n'))
# ser_bytes = ser.readline()
# print(ser_bytes)
# a = codecs.decode(ser_bytes, "ISO-8859-1").decode(ser_bytes, "UTF-8")
# print(a)
# decoded_bytes = float(ser_bytes[0:len(ser_bytes) - 2].decode("ascii"))
# print(decoded_bytes)

# b = ser.read_until(terminator='\n')
# a = ser.readlines()
# print(a)
# time.sleep(3)
# b = a.decode('utf-8')
# a = ser.read_until(terminator='\n')
# print(b)
# # print(port_chosen)
# print('Enter your commands below.\r\nInsert "exit" to leave the application.')
# # get keyboard input
# user_in = input()
# if input == 'exit':
#     ser.close()
#     exit()
# else:
#     # send the character to the device
#     # (note that I append a \r\n carriage return and line feed to the characters - this is requested by my device)
#     ser.write(str.encode(user_in + '\n'))
#     out = ''
#     # let's wait one second before reading output (let's give device time to answer)
#     time.sleep(1)
#     while True:
#         bytes_to_read = ser.in_waiting
#         ser.read(bytes_to_read)
#         # while ser.inWaiting() > 0:
#         #     # b"abcde".decode("utf-8")
#         #     data = ser.read_until()
#         #     # out = data.decode('utf-8')
#         #     out = data.decode('latin-1')
#         if bytes_to_read != '':
#             print('>>' + out)
#
# print('Flushing Data')
# ser.flush()
# time.sleep(7)
# time.sleep(6)  # logg some data
# data = []  # empty list to store the data
# for i in range(50):
#     b = ser.readline()  # read a byte string
#     string_n = b.decode(encoding='UTF-8', errors='strict')  # decode byte string into Unicode
#     string = string_n.rstrip()  # remove \n and \r
#     flt = float(string)  # convert string to float
#     print(flt)
#     data.append(flt)  # add to the end of data list
#     time.sleep(0.1)  # wait (sleep) 0.1 seconds
#
# for line in data:
#     print(line)

# p = printcore('/dev/ttyACM0', 250000)
# print('Sending M105')
# p.send_now('M154 S1')
# time.sleep(7)
# print('Sending G28')
# p.send_now('G28')
# p.send_now('M84')
# time.sleep(7)
# p.disconnect()

# movement = {}
# time.sleep(6)
# brightness_wanted = '30'  # set LED brightness str[0-255]
# ser.write(usf.set_light(brightness_wanted))
# movement.mm_wanted_y = '-100'  # move y-axis
# movement.v_wanted_y = '2500'  # set feedrate
# ser.write(bytes(b'G91\n'))
# ser.write(usf.move_printer_y(movement)
# ser.write(bytes(b'G90\n'))
# ser.write(bytes(b'M114\n'))
# ser.write(bytes(b'M105\n'))
# time.sleep(0.1)  # give the printer time to receive data
# printer_feedback = ser.readall()
# printer_feedback_decoded = printer_feedback.decode('utf-8')
# printer_feedback_decoded_list = printer_feedback_decoded.split()
# print("Temperature: ", printer_feedback_decoded_list[1])

# while True:
#     try:
#         ser.write(bytes(b'M105\n'))
#         time.sleep(2)  # give the printer time to receive data
#         printer_feedback = ser.readall()
#         printer_feedback_decoded = printer_feedback.decode('utf-8')
#         printer_feedback_decoded_list = printer_feedback_decoded.split()
#         print("Temperature: ", printer_feedback_decoded_list[1])
#         with open("test_data.csv", "a") as f:
#             writer = csv.writer(f, delimiter=",")
#             # writer.writerow([time.time(), printer_feedback_decoded_list[1]])
#             writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S", gmtime()), printer_feedback_decoded_list[1]])
#     except KeyboardInterrupt:
#         print("Keyboard Interrupt")
#         break
# print('Flushing Data')
# ser.flush()
# time.sleep(5)
# ser.write(bytes(b'M105\n'))
# ser.write(bytes(b'M117 Hello World!\n'))
# time.sleep(0.75)
# ser.write(bytes(b'G0 X 100\n'))
# ser.write(bytes(b'M105\n'))
# time.sleep(8)
# ser.write(bytes(b'M105\n'))
# time.sleep(0.75)
# ser.write(bytes(b'M105\n'))
# time.sleep(0.75)
# ser.write(bytes(b'M105\n'))
# time.sleep(0.75)
# ser.write(bytes(b'M114\n'))
# time.sleep(1)
# "Try to read line from buffer"
# a = ser.readall()
# b = a.decode('utf-8')
# print('decoded readall: ')
# print(b)

# ser_bytes = ser.readall()
# print('ser_bytes')
# print(ser_bytes)
# a = ser_bytes.decode('latin-1')
# print(a)
# # decoded_bytes = float(ser_bytes[2:len(ser_bytes) - 2].decode("ascii"))
# decoded_bytes = ser_bytes[3:len(ser_bytes) - 2].decode("ascii")
# print(decoded_bytes)

# time.sleep(7)
# brightness_wanted = '125'  # set LED brightness str[0-255]
# ser.write(usf.set_light(brightness_wanted))
# ser.write(usf.homing_printer())  # home X,Y,Z

# ser.write(bytes(b'M155 S1\n'))
# time.sleep(0.75)
# a = ser.readall()
# b = a.decode('utf-8')
# print('decoded readall: ')
# print(b)
