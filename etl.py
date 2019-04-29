import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    # open song file
    df = pd.read_json(filepath, lines = True)

    # insert song record
    song_data = df[['song_id','title','artist_id','year','duration']].values[0].tolist()
    song_data[3] = str(song_data[3])
    song_data[4] = str(song_data[4])
    
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id','artist_name','artist_location','artist_latitude','artist_longitude','artist_id']].values[0].tolist()
    if str(artist_data[3]) == "nan":
        artist_data[3] = "0.0"

    if str(artist_data[4]) == "nan":
        artist_data[4] = "0.0"
        
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    # open log file
    df = pd.read_json(filepath, lines = True)

    # filter by NextSong action
    df = df.loc[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    df['datetime'] = pd.to_datetime(df['ts'], unit='ms')
    t = df
    t['hour'] = t['datetime'].dt.hour
    t['day'] = t['datetime'].dt.day
    t['week'] = t['datetime'].dt.week
    t['month'] = t['datetime'].dt.month
    t['year'] = t['datetime'].dt.year
    t['weekday'] = t['datetime'].dt.weekday_name
    
    # insert time data records
    time_data = ("ts","hour","day","week","month","year")
    column_labels = ("start_time", "hour", "day", "week", "month", "year")
    time_df = t[["ts","hour","day","week","month","year","weekday","ts"]];
    time_df.columns = ["ts","hour","day","week","month","year","weekday","ts2"]
    time_df.head()

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[["userId","firstName","lastName","gender","level","userId"]]
    user_df.columns = ["userId","firstName","lastName","gender","level","userId2"];
    user_df = user_df.drop_duplicates(subset=["userId"],keep="first")

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, str(row.length)))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            #songid, artistid = None, None
            songid, artistid = 0, 0

        # insert songplay record
        songplay_data = [str(row.ts), str(row.userId), row.level, str(songid), str(artistid), str(row.sessionId), row.location, row.userAgent ]
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()