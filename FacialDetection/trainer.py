import cv2
import numpy as np
from PIL import Image
import os
import regex as re

path = "datasets"
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')      #Can change if doesnt work well
def getPicsAndIds(path):
    picPaths = [os.path.join(path,f) for f in os.listdir(path)]
  #  print(picPaths)
    picSamples = []
    ids = []
    for picPath in picPaths:
        PIL_pic = Image.open(picPath).convert('L') #Grayscale (cv2 works)
        pic_numpy = np.array(PIL_pic,'uint8') #Saves each image as numpy array

        m = re.findall("\d", picPath)  ###Grabs all numbers in pic and puts into array
        id = int(m[0])
        #id = int(os.path.split(picPath)[-1].split('.')[1])   #grabs id
        faces = detector.detectMultiScale(pic_numpy) #grab face


        for (x,y,w,h) in faces:
            picSamples.append(pic_numpy[y:y+h,x:x+w]) #adds to face aray
            ids.append(id) #ads to id array

    return picSamples,ids

faces,ids = getPicsAndIds(path)
recognizer.train(faces, np.array(ids))

recognizer.write("trainer/trainer.yml") #Creates yml for recognizer

print("DONE")
