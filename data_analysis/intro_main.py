import sys
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
import os
from weather import Weather
import time
from data_utils import get_dataframe, save_to_csv, process_dataframe


FIREBASE_URL = "https://monitor-a80a5.firebaseio.com/"


def main():

    weather = Weather()

    text_to_speech = TextToSpeechV1(
        username='6952ae44-af37-45dd-b83d-5a1d0c1cc785',
        password='BsjKdzv84jF8',
        x_watson_learning_opt_out=True)  # Optional flag

    def sound(text):
        with open('output.wav', 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(text, accept='audio/wav',
                                          voice="en-US_AllisonVoice")
            )
            os.system('play output.wav')

        audio_file.close()

    # welcome text
    text = 'Hi! Are you ready for tree hacks? I will monitor your productivity by tracking your tab history!'
    sound(text)

    location = weather.lookup_by_location('san jose')
    condition = location.condition()
    print(condition.text())

    text = 'Let me check the weather for you. Here you go! The weather of today in San Jose is '  + condition.temp() + 'degrees, ' + condition.text()
    sound(text)

    text = 'Seems like a less favorable day to go hang-out. Well you should probably hack hack hack.'
    sound(text)

if __name__ == '__main__':
    main()
