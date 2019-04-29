# Data Modeling with Postgres

## Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis. The data engineer will create a database schema and ETL pipeline for this analysis. The database and ETL pipeline will be tested by running queries provided by the analytics team from Sparkify and compare the outcome with expected results.

## Database Design
Star schema is be chosen to model the database to achieve song play analysis goal. The database is set up the following fact and dimension tables:

### Fact Table
**songplays** - user's song play activities

|COLUMN  	    |TYPE  	        | NOTE   	            |
|-------------- |---------------| ----------------------|
|songplay_id    |SERIAL         | Primary Key           |
|start_time     |BIGINT         | not null, foreign key |
|user_id        |INTEGER        | not null, foreign key |
|level          |VARCHAR(50)    | allow null            |
|song_id        |VARCHAR(100)   | not null, foreign key |
|artist_id      |VARCHAR(100)   | not null, foreign key |
|session_id     |INTEGER        | not null              |
|location       |VARCHAR(200)   | allow null            |
|user_agent     |TEXT           | allow null            |

### Dimension Tables
**users** - users in the app

|COLUMN  	    |TYPE  	        | NOTE   	    |
|-------------- |---------------| --------------|
|user_id        |INTEGER        | Primary Key   |
|first_name     |VARCHAR(50)    | allow null    |
|last_name      |VARCHAR(50)    | allow null    |
|gender         |VARCHAR(50)    | allow null    |
|level          |VARCHAR(50)    | allow null    |

**songs** - song data

|COLUMN  	    |TYPE  	        | NOTE   	           |
|-------------- |---------------| ---------------------|
|song_id        |VARCHAR(100)   | Primary Key          |
|title          |VARCHAR(200)   | not null             |
|artist_id      |VARCHAR(100)   | not null, foreign key|
|year           |SMALLINT       | not null             |
|duration       |NUMERIC        | not null             |

**artists** - artist data
|COLUMN  	    |TYPE  	        | NOTE   	    |
|-------------- |---------------| --------------|
|artist_id      |VARCHAR(100)   | Primary Key   |
|name           |VARCHAR(150)   | allow null    |
|location       |VARCHAR(150)   | allow null    |
|lattitude      |NUMERIC(9,5)   | allow null    |
|longitude      |NUMERIC(9,5)   | allow null    |

**time** - timestamps of records in songplays broken down into specific time units

|COLUMN  	    |TYPE  	        | NOTE   	    |
|-------------- |---------------|---------------|
|start_time     |BIGINT         | Primary Key   |
|hour           |SMALLINT       | allow null    |
|day            |SMALLINT       | allow null    |
|week           |SMALLINT       | allow null    |
|month          |SMALLINT       | allow null    |
|year           |SMALLINT       | allow null    |
|weekday        |VARCHAR(50)    | allow null    |

## Extract-Transform-Load (ETL) Pipeline
ETL pipeline is written in Python, which extract data from static text files, transform data to clean/proper data format, then load the data into related tables in the database.

The text files are in JSON format and contain data about songs, users, song play sessions/activities. The files are located in two sub-directories **"data/song_data"** and **"data/log_data"**.

## Main Files

**sql_queries.py** - contains all SQL statements that being referenced by other Python scripts.

**create_tables.py** - contains functions to establish database connection and rebuild database schema using drops & creates SQL statements. Run this file if the database need a clean up/rest before the ETL scripts are run.

**etl.py** - contains functions to read and process files from "song_data" and "log_data" and loads data into database. 

## Other Dev Files
**etl.ipynb** - Jupyper notebook contains methods to test ETL processes
**test.ipynb** - Jupyper notebook contains methods to check/validate data in the database
