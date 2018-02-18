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

def save_to_csv(df):
    path = 'data/activity.csv'
    print('[*] Saving dataframe to %s' % path)
    df.to_csv(path)

def process_dataframe(df):
    try:
        from urllib.parse import urlparse
    except:
        from urlparse import urlparse
    # parse hostnames, paths, and time spent on tab
    print('[*] Writing engineered features to dataframe')
    urlobjs = [urlparse(df.iloc[i]['url']) for i in range(len(df))]
    hostnames = [obj.hostname for obj in urlobjs]
    paths = [obj.path for obj in urlobjs]
    times = [df.iloc[i]['endTime'] - df.iloc[i]['startTime'] for i in range(len(df))]
    df['hostname'] = pd.Series(hostnames)
    df['path'] = pd.Series(paths)
    df['time'] = pd.Series(times)
    return df
