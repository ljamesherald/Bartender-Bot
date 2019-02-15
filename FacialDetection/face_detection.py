import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)             #starts video
count = 0
face_id = input('\n Enter use id end press lasldsad')
while(True):

# Captures img-by-img and is greyscale(how CV2 works)
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x,y,w,h) in faces:
#        print(x,y,w,h)
        color = (255, 0, 0)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(img, (x,y), (end_cord_x, end_cord_y), color, stroke) #creates rectangle around face
        count +=1
        cv2.imwrite("datasets/User." + str(face_id) + '.' + str(count) + '.jpg', gray[y:y+h,x:x+w]) #stores jpgs into datasets folder... need to create datasets folder
        cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xFF       #ESC key should allow to exit
    if k == 27:
        break
    elif count >= 5:                  #Grabs 5 pics of face and then exits
        break
#Displays resulting img in actual color

#Create Trainer

#Create Recognizer

cap.release()
cv2.destroyAllWindows()
