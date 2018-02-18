import pandas as pd
from firebase import firebase


def get_dataframe(firebase_url):
    print('[*] Opening connection to Firebase')
    fb = firebase.FirebaseApplication(firebase_url, None)
    result = fb.get('', None)
    result = list(result['activity'].values())
    print('[*] Converting python object to dataframe')
    result_columns = {key: [row[key] for row in result] for key in result[0]}
    df = pd.DataFrame(result_columns)
    return df

def download_csv(firebase_url):
    path = 'data/activity.csv'
    df = get_dataframe(firebase_url)
    print('[*] Saving tab activity to %s' % path)
    df.to_csv(path)
