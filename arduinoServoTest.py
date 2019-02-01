from BreakfastSerial import Arduino
from components import *
from time import sleep

board = Arduino('/dev/cu.usbmodem1421')
s = Servo(board, 9)

position = s.value
counter = 0



while True:
    cmd = input("command: ")

    if cmd == "left":

        while counter < 5:
            counter += 1
            if (position == 0):
                position = 180
            new_position = position-1
            s.set_position(new_position)
            position = new_position
            sleep(5)

    elif cmd == "right":

        while counter < 5:
            counter += 1
            if (position == 180):
                position = 0
            new_position = position+1
            s.set_position(new_position)
            position = new_position
            sleep(5)

    elif cmd == "q":
        break
    else:
        print("command not recognized")