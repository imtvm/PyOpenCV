import cv2
import numpy as np

cap = cv2.VideoCapture(0) #Sets the video input to the main webcam

#Rescaling the video capture frame

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

#Actually displaying the video capture

while True:
    ret, frame = cap.read() #reads the video capture

    greyscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #changes the frame to greyscale

    frame = rescale_frame(frame, percent=30)

    cv2.imshow("frame", frame) #shows the regualar frame
    #cv2.imshow("frame2", greyscale) #shows the greyscale frame

    if cv2.waitKey(20) & 0xFF == ord('q'): #tells the window to quit when q is pressed
        break
