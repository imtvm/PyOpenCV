import cv2
import numpy as np

face_cas = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml') #the file you need to recoginze faces can be swapped out for the other ones in the data file

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

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey = rescale_frame(grey, 45)
    frame = rescale_frame(frame, 45)

    faces = face_cas.detectMultiScale(grey, scaleFactor=1.05, minNeighbors=5) #is what actually detects the face the numbers can be changed for more accuracy

    for (x, y, w, h) in faces: #x y  are the x and y positions of the bottom left of the face and w and h are the width and height
        roi_grey = grey[y:y+h, x:x+w] #combingin them gives the enitre region of the face. this one is grey scale
        roi_color = frame[y:y+h, x:x+w] #this one is in color
        grey_cap = "grey_cap.png"
        color_cap = "color_cap.png"
        #cv2.imwrite(grey_cap, roi_grey) #this saves the grey scale image
        #cv2.imwrite(color_cap, roi_color) #this saves the color image

        color = (255, 0, 0) #BGR. this is going to set the color of the box we are going to draw around the face
        stroke = 2 #this is the thickness of the lines that draw the box
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, stroke) #draws the rectangle on the frame


    cv2.imshow("frame", frame) #shows the regualar frame

    if cv2.waitKey(20) & 0xFF == ord('q'): #tells the window to quit when q is pressed
        break

#releases the capture when everything is done (idk what this does tho look it up later)
cap.release()
cv2.destroyAllWindows()