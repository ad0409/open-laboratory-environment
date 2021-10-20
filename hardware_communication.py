#!/usr/bin/env python3
import mraa
import time

# pin_no = 32
# # Export the GPIO pin for use
# pin = mraa.Gpio(pin_no)
# # Small delay to allow udev rules to execute (necessary only on up)
# time.sleep(0.1)
# # Configure the pin direction
# pin.dir(mraa.DIR_OUT)
#
#
# def led_on():
#     pin.write(1)
#     print('hardware_led_on')
#
#
# def led_off():
#     pin.write(0)
#     print('hardware_led_off')
#
#
# if __name__ == '__main__':
#     print('AN')
#     led_on()
#     time.sleep(1)
#     print('AUS')
#     led_off()


ledPin = 32
led = mraa.Pwm(ledPin)
led.enable(True)


def led_on():
    print('hardware_led_on')
    duty = 0.0
    try:
        while 1:
            while duty < 1.0:
                print('hardware_led_UP')
                led.write(duty)
                duty += 0.05
                time.sleep(0.1)
            while duty > 0.0:
                print('hardware_led_DOWN')
                led.write(duty)
                duty -= 0.05
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass

    led.write(0)
    led.enable(False)


def led_off():
    led.write(0)
    print('hardware_led_off')


if __name__ == '__main__':
    print('AN')
    led_on()
    time.sleep(1)
    print('AUS')
    led_off()

