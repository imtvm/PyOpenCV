import os
from PIL import Image
import numpy as np
import pickle
import cv2

face_cas = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml') #loads the face casscade

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #gets the base dir that the facesTrain.py file is in
image_dir = os.path.join(BASE_DIR, "images") #finds the folder with all the images

recognizer = cv2.face.LBPHFaceRecognizer_create() #this is the train(ed)[able] face recognizer that is provided with open cv

current_id = 0 # id counter
label_ids = {} #dicontary (associative array)
x_train = [] # array of the photo values
y_labels = [] #array of the ids

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith(".png") or file.endswith(".jpg"): #looks for files that end with jpg or png
            path = os.path.join(root, file) #gets the path of the image
            label = os.path.basename(root).replace(" ", "-").lower() #gets the name fo the dir that contains the image
            # print(label)
            if not label in label_ids: #sets the labels to an id
                label_ids[label] = current_id
                current_id += 1

            id_ = label_ids[label]
            print(label_ids)
            pil_image = Image.open(path).convert("L") #opens the image and then converts it into grey scale
            image_array = np.array(pil_image, "uint8") #lits all the image data in a numpy array with the encoding of uint8
            # print(image_array)
            faces = face_cas.detectMultiScale(image_array, scaleFactor=1.05, minNeighbors=5) #what actually detects the faces
            for x, y, w, h in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)

# print(y_labels)
# print(x_train)

with open("labels.pickle", 'wb') as f: #creates a pickle file with all the labels and the ids
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels)) #trains the recognizer
recognizer.save("trainer.yml") #creates the trainer file

