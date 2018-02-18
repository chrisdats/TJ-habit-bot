import sys

from data_utils import get_dataframe, save_to_csv, process_dataframe


FIREBASE_URL = "https://monitor-a80a5.firebaseio.com/"

def main():
    df = process_dataframe(get_dataframe(FIREBASE_URL))
    print('Last five rows:\n', df[-5:][['url', 'time']], '\n')
    save_to_csv(df)

if __name__ == '__main__':
    main()
