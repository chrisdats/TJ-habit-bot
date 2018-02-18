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

def compute_metrics(df):
    hostname_times = pd.Series()
    for i in range(len(df)):
        row = df.iloc[i]
        hostname = row['hostname']
        if hostname in hostname_times.keys():
            hostname_times[hostname] += row['time']
        else:
            hostname_times[hostname] = row['time']
    hostname_times = hostname_times.sort_values(ascending=False)

    TIME_MULT = 3600000

    rows = []
    start_time = df.iloc[0]['startTime']
    time = df.iloc[0]['endTime']
    for i in range(len(df)):
        entry = df.iloc[i]
        rows.append([(entry['startTime']-start_time)/TIME_MULT, entry['time']/TIME_MULT, entry['hostname']])
        time = entry['endTime']

    WORK_HOSTS = [
        'github.com',
        'matplotlib.org',
        'pandas.pydata.org',
        'stackoverflow.com',
        'console.firebase.google.com',
        'bokeh.pydata.org',
        'pymotw.com',
        'localhost',
        'www.google.com'
    ]
    MEDIA_HOSTS = [
        'www.youtube.com',
        'www.reddit.com',
        'www.facebook.com',
        'www.businessinsider.com',
        'mail.google.com'
    ]

    x_work, x_media, x_other = [], [], []
    width_work, width_media, width_other = [], [], []
    for row in rows:
        if row[2] in WORK_HOSTS:
            x_work.append(row[0])
            width_work.append(row[1])
        elif row[2] in MEDIA_HOSTS:
            x_media.append(row[0])
            width_media.append(row[1])
        else:
            x_other.append(row[0])
            width_other.append(row[1])
    
    return {
        'time_work': sum(width_work),
        'time_media': sum(width_media),
        'time_other': sum(width_other),
        'top_hosts': list(hostname_times.keys())
    }
    