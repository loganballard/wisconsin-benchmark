import psycopg2 as pgre
from os import environ as env

def get_setup_vars():
    return {
        'db': env['P_DB'] if env.get('P_DB') else 'wisc',
        'host': env['P_HOST'] if env.get('P_HOST') else 'localhost',
        'port': env['P_PORT'] if env.get('P_PORT') else 5432,
        'user': env['P_USER'] if env.get('P_USER') else 'postgres',
        'pass': env['P_PASS'] if env.get('P_PASS') else 'admin'
    }

# decorator that will do all the try/catching for pyscopg2
# sql errors
def transaction(db_call):
    def transaction_wrapper(conn, *args, **kwargs):
        try:
            cursor = conn.cursor()
            db_call(cursor, *args, **kwargs)
            cursor.close()
            conn.commit()
        except pgre.DatabaseError as error:
            conn.rollback()
            print(error)
    return transaction_wrapper

@transaction
def create_schema(cursor, schema):
    """
    Make sure to pass in a connection object when calling! 
    Decorator will pass in cursor.
    Creates the named schema.
    
    Arguments:
        - cursor (conn) - a postgres connection object
        - schema - name of the schema to be created
    """
    cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema};")

@transaction
def create_tables(cursor, schema):
    """
    Make sure to pass in a connection object when calling!
    Creates the tables that the wisconsin benchmark tests: 1k, 10k, 10k2
    
    Arguments:
        - cursor (conn) - a postgres connection object
        - schema - name of the schema
    """
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {schema}.ONEKTUP (
        unique1         integer NOT NULL,
        unique2         integer NOT NULL PRIMARY KEY,
        two             integer NOT NULL,
        four            integer NOT NULL,
        ten             integer NOT NULL,
        twenty          integer NOT NULL,
        onePercent      integer NOT NULL,
        tenPercent      integer NOT NULL,
        twentyPercent   integer NOT NULL,
        fiftyPercent    integer NOT NULL,
        unique3         integer NOT NULL,
        evenOnePercent  integer NOT NULL,
        oddOnePercent   integer NOT NULL,
        stringu1        char(52) NOT NULL,
        stringu2        char(52) NOT NULL,
        string4         char(52) NOT NULL
    );""")
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {schema}.TENKTUP1 (
        unique1         integer NOT NULL,
        unique2         integer NOT NULL PRIMARY KEY,
        two             integer NOT NULL,
        four            integer NOT NULL,
        ten             integer NOT NULL,
        twenty          integer NOT NULL,
        onePercent      integer NOT NULL,
        tenPercent      integer NOT NULL,
        twentyPercent   integer NOT NULL,
        fiftyPercent    integer NOT NULL,
        unique3         integer NOT NULL,
        evenOnePercent  integer NOT NULL,
        oddOnePercent   integer NOT NULL,
        stringu1        char(52) NOT NULL,
        stringu2        char(52) NOT NULL,
        string4         char(52) NOT NULL
    );""")
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {schema}.TENKTUP2 (
        unique1         integer NOT NULL,
        unique2         integer NOT NULL PRIMARY KEY,
        two             integer NOT NULL,
        four            integer NOT NULL,
        ten             integer NOT NULL,
        twenty          integer NOT NULL,
        onePercent      integer NOT NULL,
        tenPercent      integer NOT NULL,
        twentyPercent   integer NOT NULL,
        fiftyPercent    integer NOT NULL,
        unique3         integer NOT NULL,
        evenOnePercent  integer NOT NULL,
        oddOnePercent   integer NOT NULL,
        stringu1        char(52) NOT NULL,
        stringu2        char(52) NOT NULL,
        string4         char(52) NOT NULL
    );""")
