import sys

from data_utils import get_dataframe, download_csv


FIREBASE_URL = "https://monitor-a80a5.firebaseio.com/"

def main():
    df = get_dataframe(FIREBASE_URL)
    print(df[-5:]['url'])
    download_csv(FIREBASE_URL)

if __name__ == '__main__':
    main()
