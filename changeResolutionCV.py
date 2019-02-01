import cv2
import numpy as np

cap = cv2.VideoCapture(0) #Sets the video input to the main webcam

#Making it different resolutions:

def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(cin, width, height):
    cin.set(3, width)
    cin.set(4, height)

make_480p()

#Actually displaying the video capture

while True:
    ret, frame = cap.read() #reads the video capture

    greyscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #changes the frame to greyscale

    cv2.imshow("frame", frame) #shows the regualar frame
    #cv2.imshow("frame2", greyscale) #shows the greyscale frame

    if cv2.waitKey(20) & 0xFF == ord('q'): #tells the window to quit when q is pressed
        break

#releases the capture when everything is done (idk what this does tho look it up later)
cap.release()
cv2.destroyAllWindows()