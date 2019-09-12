#!/usr/bin/env python3

import speech_recognition as sr
from os import path
# obtain path to "english.wav" in the same folder as this script
def audio_extract (AUDIO_FILE):
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Sphinx
    try:
        file = open("data.txt","w") 
        text = r.recognize_sphinx(audio)
        file.writelines(text)
        file.close()
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
        
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")

audio_extract(AUDIO_FILE)