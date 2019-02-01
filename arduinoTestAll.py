from BreakfastSerial import Arduino
from components import *
from time import sleep

board = Arduino("/dev/cu.usbmodem1421")
up_led = Led(board, 9)
down_led = Led(board, 7)
left_led = Led(board, 4)
right_led = Led(board, 8)

def all_on():
    down_led.on()
    up_led.on()
    right_led.on()
    left_led.on()

def all_off():
    down_led.off()
    up_led.off()
    right_led.off()
    left_led.off()

while True:
    cmd = input("command: ")

    if cmd == "on":
        all_on()
    elif cmd == "off":
        all_off()
    elif cmd == "q":
        all_off()
        break
    else:
        print("command not recognized")
