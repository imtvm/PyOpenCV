from BreakfastSerial import Arduino
from components import *
from time import sleep

board = Arduino('/dev/cu.usbmodem1421')
s = Servo(board, 9)
s.reset()

while True:
    cmd = input("command: ")

    if cmd != "q":
        s.set_position(cmd)
    else:
        s.reset()
        break