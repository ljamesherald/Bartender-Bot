import io
import os
import SpeachRecognition
import speech_recognition as sr
import time

r = sr.Recognizer()

# Words that sphinx should listen closely for. 0-1 is the sensitivity
# of the wake word.
keywords = [("bartender", 1)]

source = sr.Microphone()

def callback(recognizer, audio):  # this is called from the background thread

    try:
        speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=keywords)
        print(speech_as_text)

        # Look for your "bartender" keyword in speech_as_text
        if "bartender" in speech_as_text:
            recognize_main()

    except sr.UnknownValueError:
        print("Oops! Didn't catch that")


def recognize_main():
    print("Recognizing Main...")
    audio_data = r.listen(source)
    print(audio_data)
    # interpret the user's words however you normally interpret them


def start_recognizer():
    r.listen_in_background(source, callback)
    time.sleep(1000000)


start_recognizer()
