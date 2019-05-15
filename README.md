# Logan's Wisconsin Benchmark

My attempt to recreate the Wisconsin Benchmark is PostGreSQL.  I know that postgres has this implemented already, but this is a good DB exercise.

## Pre-requisite Setup

Set environment variables that contain Postgres information.  You'll need access to a postgres database as well a user with read and write capabilities.

#### Environment Variables
    - P_HOST: Name of postgres host.  Defaults to localhost
    - P_DB: Name of postgres db. Defaults to wisc
    - P_PORT: Postgres port. Defaults to 5432
    - P_USER: Postgres Username.  Defaults to postgres
    - P_PASS: Postgres Password. Defaults to admin

Set up a python environment that will use `psycopg2` and allow programmatic postgres integration.

#### Python Environment
1. [Install python3.6+ and pip](https://www.makeuseof.com/tag/install-pip-for-python/)
2. [Create a python virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
    - Depending on your OS, this will look different.  On Windows: `python -m virtualenv venv`
3. Activate the virtual environment
    - Depending on your OS, this will look different.  On Windows: `.\venv\Scripts\Activate`
4. `pip install -r requirements.txt`

## Part 1 - Initial Table Creation and Data Population

In this section, I'll be creating the tables in postgres, and creating data generation code.  The DB that I've chosen is PostGreSQL because of my familiarity with it, its vast use and support in the DB community, and widely available programming language support.

I'll be using Python for data generation due to my familiarty with it and ease of scripting.  The thoroughly documented [psycopg2](http://initd.org/psycopg/docs/) python library is easy to use and integrates well.

The intial population is all done with a python driver. It allows setting of all postgres-related variables that are necessary for connections.  It also will populate all of the necessary data for analysis according to the wisconsin benchmark.

### Driver Usage

To use the driver, call it with `python main.py`.  It accepts two flags that will be useful:

- __-c__ 
    - The `--creds` flag will set the environment variables necessary for postgres connections according to user input.
- __-p__ 
    - The `--populate` flag will build a schema, tables, and randomized data that lives in those tables.
        - Schema name will be determined by user input
        - Tables are created according to the [Wisconsin Benchmark specification](http://jimgray.azurewebsites.net/benchmarkhandbook/chapter4.pdf): `onektup`, `tenktup1`, `tenktup2`.

#### Example Tuples from `onektup`:
```
"unique1","unique2","two","four","ten","twenty","onepercent","tenpercent","twentypercent","fiftypercent","unique3","evenonepercent","oddonepercent","stringu1","stringu2","string4"
1888,0,0,0,8,8,88,8,3,0,1888,176,177,"AAAACUQxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","AAAAAAAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","AAAAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
8140,1,0,0,0,0,40,0,0,0,8140,80,81,"AAAAMBCxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","AAAAAABxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","HHHHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
9000,2,0,0,0,0,0,0,0,0,9000,0,1,"AAAANIExxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","AAAAAACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","OOOOxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
4925,3,1,1,5,5,25,5,0,1,4925,50,51,"AAAAHHLxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","AAAAAADxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","VVVVxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
1734,4,0,2,4,14,34,4,4,0,1734,68,69,"AAAACOSxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","AAAAAAExxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","AAAAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
1925,5,1,1,5,5,25,5,0,1,1925,50,51,"AAAACWBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","AAAAAAFxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","HHHHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
...
(994 more)
...
```

### Lessons Learned from Part 1

- Make sure to figure out how to make postgres connections before trying to write the SQL necessary to do data population
- Test with tiny subset before trying to populate the entire database

## Part 2: Benchmarks

In order to accurately use this database, it is necessary to develop several queries that will accurately test database performance.  The goal of this portion of the Wisconsin Benchmark is to produce queries that will gauge the performance of database systems in measureable and valuable ways.

In this set of experiments, I will test how postgres performs when configured with a variety of different tests.  See the [performance-test-plan](./performance-test-plan) folder for more.