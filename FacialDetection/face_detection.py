
import cv2
import os
import SpeachRecognition as sm
import speech_recognition as sr
import regex as re


face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
path = "datasets"
picPaths = [os.path.join(path,f) for f in os.listdir(path)]
cam = cv2.VideoCapture(0)
count = 0
face_id = 0
#name = input("What is your name?")
recognizer = sr.Recognizer()
microphone = sr.Microphone()


print("What is your name?")
name = sm.recognize_speech_from_mic(recognizer, microphone)["transcription"]


for picPath in picPaths:          #Gives each User unique Id number
    m = re.findall("\d", picPath)         ###Grabs all numbers in pic and puts into array
    n = int(m[0])                     ###Takes first number from array turns to int
    while(face_id == n):
        face_id = face_id + 1

print("Please wait while we capture our facial Data...")

while True:

# Captures img-by-img and is greyscale(how CV2 works)
    ret, img = cam.read()
    cv2.imshow("image", img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    if ret == True:
        for (x,y,w,h) in faces:
            color = (255, 0, 0)
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            count +=1
            print("Captured " + str(count) + "!")
            cv2.imwrite("datasets/" + str(face_id) + '.' + str(name) + '.' + str(count) + '.jpg', gray[y:y+h,x:x+w]) #stores jpgs into datasets folder... need to create datasets folder
        k = cv2.waitKey(100) & 0xFF       #ESC key should allow to exit
        if k == 27:
            break
        elif count >= 10:                  #Grabs 15 pics of face and then exits
            break

cam.release()
cv2.destroyAllWindows()
