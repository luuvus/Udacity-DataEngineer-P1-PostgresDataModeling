# TABLE NAMES
TBL_SONGPLAYS = "songplays"
TBL_USERS = "users"
TBL_SONGS = "songs"
TBL_ARTISTS = "artists"
TBL_TIME = "time"

# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS " + TBL_SONGPLAYS
user_table_drop = "DROP TABLE IF EXISTS " + TBL_USERS
song_table_drop = "DROP TABLE IF EXISTS " + TBL_SONGS
artist_table_drop = "DROP TABLE IF EXISTS " + TBL_ARTISTS
time_table_drop = "DROP TABLE IF EXISTS " + TBL_TIME

# CREATE TABLES

songplay_table_create = ("CREATE TABLE IF NOT EXISTS " + 
                         TBL_SONGPLAYS + " ( " + 
                         "songplay_id SERIAL PRIMARY KEY," + 
                         "start_time BIGINT NOT NULL," + 
                         "user_id INTEGER NOT NULL," + 
                         "level VARCHAR(50) NULL," + 
                         "song_id  VARCHAR(100) NOT NULL," + 
                         "artist_id  VARCHAR(100) NOT NULL," + 
                         "session_id INTEGER NOT NULL," + 
                         "location VARCHAR(200) NULL," + 
                         "user_agent TEXT NULL" + 
                        ")")

user_table_create =  ("CREATE TABLE IF NOT EXISTS " + 
                         TBL_USERS + " ( " + 
                         "user_id INTEGER PRIMARY KEY," + 
                         "first_name VARCHAR(50) NULL," + 
                         "last_name VARCHAR(50) NULL," + 
                         "gender VARCHAR(50) NULL," + 
                         "level VARCHAR(50) NULL" + 
                        ")")
song_table_create = ("CREATE TABLE IF NOT EXISTS " + 
                         TBL_SONGS + " ( " + 
                         "song_id VARCHAR(100) PRIMARY KEY," + 
                         "title VARCHAR(200) NOT NULL," + 
                         "artist_id VARCHAR(100) NOT NULL," + 
                         "year SMALLINT," + 
                         "duration NUMERIC" + 
                        ")")
artist_table_create = ("CREATE TABLE IF NOT EXISTS " + 
                         TBL_ARTISTS + " ( " + 
                         "artist_id VARCHAR(100) PRIMARY KEY," + 
                         "name VARCHAR(150) NULL," + 
                         "location VARCHAR(150) NULL," + 
                         "lattitude NUMERIC(9,5) NULL," + 
                         "longitude NUMERIC(9,5) NULL" + 
                        ")")
time_table_create = ("CREATE TABLE IF NOT EXISTS " + 
                         TBL_TIME + " ( " + 
                         "start_time BIGINT NOT NULL PRIMARY KEY," + 
                         "hour SMALLINT NULL," + 
                         "day SMALLINT NULL," + 
                         "week SMALLINT NULL," + 
                         "month SMALLINT NULL," + 
                         "year SMALLINT NULL," + 
                         "weekday VARCHAR(50)" + 
                        ")")

# INSERT RECORDS

songplay_table_insert = ("INSERT INTO " + TBL_SONGPLAYS + 
                         "(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) " + 
                         "VALUES " + 
                         "(%s, %s, %s, %s, %s, %s, %s, %s)")

user_table_insert_1 = ("INSERT INTO " + TBL_USERS + 
                         "(user_id,first_name, last_name, gender, level)" + 
                         "VALUES " + 
                         "(%s, %s, %s, %s, %s)")

user_table_insert = ("INSERT INTO " + TBL_USERS + 
                         "(user_id,first_name, last_name, gender, level) " + 
                         "SELECT %s, %s, %s, %s, %s " + 
                         " WHERE NOT EXISTS (" + 
                         "      SELECT 1 FROM " + TBL_USERS + " WHERE user_id= %s " + 
                         ")")

song_table_insert = ("INSERT INTO " + TBL_SONGS + 
                         "(song_id, title, artist_id, year, duration)" + 
                         "VALUES " + 
                         "(%s, %s, %s, %s, %s)")

artist_table_insert_1 = ("INSERT INTO " + TBL_ARTISTS + 
                         "(artist_id,name, location, lattitude, longitude)" + 
                         "VALUES " + 
                         "(%s, %s, %s, %s, %s)")

artist_table_insert = ("INSERT INTO " + TBL_ARTISTS + 
                         "(artist_id,name, location, lattitude, longitude) " + 
                         "SELECT %s, %s, %s, %s, %s " + 
                         " WHERE NOT EXISTS (" + 
                         "      SELECT 1 FROM " + TBL_ARTISTS + " WHERE artist_id= %s " + 
                         ")")

time_table_insert_1 = ("INSERT INTO " + TBL_TIME + 
                         "(start_time, hour, day, week, month, year, weekday)" + 
                         "VALUES " + 
                         "(%s, %s, %s, %s, %s, %s, %s)")

time_table_insert = ("INSERT INTO " + TBL_TIME + 
                         "(start_time, hour, day, week, month, year, weekday) " + 
                         "SELECT %s, %s, %s, %s, %s, %s, %s " + 
                         " WHERE NOT EXISTS (" + 
                         "      SELECT 1 FROM " + TBL_TIME + " WHERE start_time = %s " + 
                         ")")
# FIND SONGS

song_select = ("SELECT * FROM " + TBL_SONGS + " WHERE title = %s AND artist_id = %s AND duration = %s")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create,artist_table_create, song_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]