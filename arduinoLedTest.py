from BreakfastSerial import Arduino
from components import *

board = Arduino("/dev/cu.usbmodem1411")
pin = 12
led = Led(board, pin)

while True:
    cmd = input("command: ")

    if cmd == "on":
        led.on()
    elif cmd == "off":
        led.off()
    elif cmd == "q":
        break
    else:
        print("command not recognized")
