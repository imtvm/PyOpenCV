import cv2
import numpy as np

cap = cv2.VideoCapture(0) #Sets the video input to the main webcam

#Actually displaying the video capture

while True:
    ret, frame = cap.read() #reads the video capture

    cv2.imshow("frame", frame) #shows the regualar frame

    if cv2.waitKey(20) & 0xFF == ord('q'): #tells the window to quit when q is pressed
        break

#releases the capture when everything is done (idk what this does tho look it up later)
cap.release()
cv2.destroyAllWindows()