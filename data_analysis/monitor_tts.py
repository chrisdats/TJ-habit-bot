# coding=utf-8
from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
import os
from weather import Weather
import time
import threading

def sound(text):
    with open('output.wav', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(text, accept='audio/wav',
                                      voice="en-US_AllisonVoice")
        )
        os.system('play output.wav')
    audio_file.close()

weather = Weather()

text_to_speech = TextToSpeechV1(
    username='6952ae44-af37-45dd-b83d-5a1d0c1cc785',
    password='BsjKdzv84jF8',
    x_watson_learning_opt_out=True)  # Optional flag

text = 'Hi! Are you ready for tree hacks?'
sound(text)

#os.system('play output.wav')

location = weather.lookup_by_location('san jose')
condition = location.condition()
print(condition.text())



text = 'The weather of today is ' + condition.temp() + 'degrees, ' + condition.text()
sound(text)

text = 'Why bother go out when you can hack?'
sound(text)


# time spent on site
# time spent 




