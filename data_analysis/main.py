from pull_data import get_df

def main():
    df = get_df()
    print(df[-5:])
    print(len(df))

if __name__ == '__main__':
    main()
