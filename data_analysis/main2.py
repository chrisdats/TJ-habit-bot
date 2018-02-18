import sys
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
import os
import time
from data_utils import get_dataframe, save_to_csv, process_dataframe, compute_metrics
from weather import Weather
import pickle


FIREBASE_URL = "https://monitor-a80a5.firebaseio.com/"

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

def main():
    weather = Weather()
    df = process_dataframe(get_dataframe(FIREBASE_URL))

    print('Last five rows:\n', df[-5:][['url', 'time']], '\n')
    save_to_csv(df)
    text = 'Hi! Here is how you have been doing so far.'
    sound(text)

    results = compute_metrics(df)
    #print(results)
    time_work = str(10.03)
    time_media = str(0.69)
    time_other = str(1.78)
    top_hosts = ['localhost', 'google', 'firebase console']
    text = 'You spend ' + time_work + 'hours on work tab, ' + time_media + ' hours on media and ' + time_other + 'hours on other.' \
          + 'Your top three tabs are: ' + top_hosts[0] + ', ' + top_hosts[1] + ',' + top_hosts[2]
    sound(text)


if __name__ == '__main__':
    main()
