# Wisconsin Benchmark

My attempt to recreate the Wisconsin Benchmark is PostGreSQL.  I know that postgres has this implementation already, but this is a good DB exercise.

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