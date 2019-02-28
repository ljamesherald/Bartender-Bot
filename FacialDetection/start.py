import os

answer = input("Are you a new or returning Customer?")
if(answer == "new"):
#    os.system('py -3 face_detection.py')
    os.system('py -3 trainer.py')
    os.system('py -3 recognizer.py')
else:
    os.system('py -3 recognizer.py')
