#!/usr/bin/env python3

import speech_recognition as sr
from os import path
from hatesonar import Sonar
import json
import sys

# obtain path to "english.wav" in the same folder as this script
def audio_extract (AUDIO_FILE):
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Sphinx
    try:
       
        text = r.recognize_sphinx(audio)      
        f = open('data.txt', 'a+')
        f.write(text + ',\n')
        f.close()
        return (text)
    except sr.UnknownValueError:
        return("Sphinx could not understand audio")
    except sr.RequestError as e:
        return("Sphinx error; {0}".format(e))

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), sys.argv[1])
print(AUDIO_FILE)

TEXT = audio_extract(AUDIO_FILE)



