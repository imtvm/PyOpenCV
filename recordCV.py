import cv2
import numpy as np
import os

#changing the resolution of whatever frame given

def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

#The basic dimensions

STD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

#getting the proper dimensions and the sets it to the capture

def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSIONS['480p'] #defaults the dimensions to 480p incase the value you set res to does not exist
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    change_res(cap, width, height)
    return width, height


#setting the codex of the video type

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

#gets the video type to check it against the key array above

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']

#setting up all the variables that is needed to record as well as display the capture

filename = "testvideo.mp4" # .avi and .mp4 are the main files to work with
fps = 24.0 #frame rate
res = '720p' #can use other ones as well like 1080p

cap = cv2.VideoCapture(0) #Sets the video input to the main webcam
dims = get_dims(cap, res=res)
video_type = get_video_type(filename)

#setting up the recording

out = cv2.VideoWriter(filename, video_type, fps, dims)

#Actually displaying the video capture

while True:
    ret, frame = cap.read() #reads the video capture

    greyscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #changes the frame to greyscale

    out.write(frame) #actually recording

    cv2.imshow("frame", frame) #shows the regualar frame
    #cv2.imshow("frame2", greyscale) #shows the greyscale frame

    if cv2.waitKey(20) & 0xFF == ord('q'): #tells the window to quit when q is pressed
        break

#releases the capture when everything is done (idk what this does tho look it up later)
cap.release()
cv2.destroyAllWindows()
out.release()