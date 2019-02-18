

import cv2
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')                          #cv2 reads yml
cascadePath = 'cascades/data/haarcascade_frontalface_alt2.xml'
faceCascade = cv2.CascadeClassifier(cascadePath)
path = "datasets"
picPaths = [os.path.join(path,f) for f in os.listdir(path)]
font = cv2.FONT_HERSHEY_SIMPLEX
names = []
#iniciate id counter
id = 0

uid = 0
for picPath in picPaths:
    if(uid == int(os.path.split(picPath)[-1].split('.')[1])):
        name = picPath[picPath.find('\\')+1 : picPath.find('.')]
        uid = uid + 1
        names.append(name)               #print each name to the names array names array is mapped to ID

#print(names)

cam = cv2.VideoCapture(0)


while True:

    ret, img = cam.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < 100):
            id = names[id]                         #maps name to id
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
        print("You are " + str(id))

    cv2.imshow('camera',img)


    k = cv2.waitKey(10) & 0xff # ESC to exit
    if k == 27:
        break

print("\n Exiting Program")
cam.release()
cv2.destroyAllWindows()
