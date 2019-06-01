import psycopg2 as pgre
from os import environ as env
from random import sample

def get_setup_vars():
    return {
        'db': env['P_DB'] if env.get('P_DB') else 'wisc',
        'host': env['P_HOST'] if env.get('P_HOST') else 'localhost',
        'port': env['P_PORT'] if env.get('P_PORT') else 5432,
        'user': env['P_USER'] if env.get('P_USER') else 'postgres',
        'pass': env['P_PASS'] if env.get('P_PASS') else 'admin'
    }

def transaction(db_call):
    """
    decorator that will do all the try/catching for pyscopg2
    sql errors

    Pass in a function that takes a CONNECTION as an argument
    and then any other arguments.  Note that this will return a
    function that takes a CURSOR as an argument, so in the 
    function definition, a CURSOR must be used, but when
    decorated and used, a CONNECTION must be passed
    """
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
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {schema}.HUNDREDKTUP1 (
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

@transaction
def insert_tuple(cursor, vals, schema, table):
    """
    Make sure to pass in a connection object when calling!
    Creates the tables that the wisconsin benchmark tests: 1k, 10k, 10k2
    
    Arguments:
        - cursor (conn) - a postgres connection object
        - vals - the tuple to insert
        - schema - name of the schema
        - table - the table to insert the tuple into
    """
    cursor.execute(f"""
        INSERT INTO {schema}.{table} (unique1, unique2, two, four, ten, twenty, onePercent, tenPercent, twentyPercent, fiftyPercent, unique3, evenOnePercent, oddOnePercent, stringu1, stringu2, string4)
        VALUES ({vals[0]}, {vals[1]}, {vals[2]}, {vals[3]}, {vals[4]}, {vals[5]}, {vals[6]}, {vals[7]}, {vals[8]}, {vals[9]}, {vals[10]}, {vals[11]}, {vals[12]}, '{vals[13]}', '{vals[14]}', '{vals[15]}');
    """)

def gen_stringu1_2(uniq):
    ret = ['A','A','A','A','A','A','A']
    i = 6
    while uniq > 0:
        rem = uniq % 26
        ret[i] = chr(ord('A') + rem)
        uniq = uniq // 26
        i -= 1
    return "".join(ret) + 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

def gen_string4(x):
    string4 = [
        'AAAAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'HHHHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'OOOOxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'VVVVxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    ]
    return string4[x % 4]


def build_vals_tup(uniq2, table_size):
    """

    """
    uniq1 = uniq3 = table_size[uniq2]
    two = fiftyP = uniq1 % 2
    four = uniq1 % 4
    ten = tenP = uniq1 % 10
    twenty = uniq1 % 20
    oneP = uniq1 % 100
    twentyP = uniq1 % 5
    evenOneP = oneP*2
    oddOneP = evenOneP + 1
    stringu1 = gen_stringu1_2(uniq1)
    stringu2 = gen_stringu1_2(uniq2)
    string4 = gen_string4(uniq2)
    return (uniq1, uniq2, two, four, ten, twenty, oneP, tenP, twentyP, fiftyP, uniq3, evenOneP, oddOneP, stringu1, stringu2, string4)



def generate_data(conn, schema):
    """
    Generates fake data to be inserted into the 1k, tenk1, tenk2,
    tables.

    Arguments:
        - cursor (conn) - a postgres connection object
        - schema - name of the schema
    """
    one_thous = sample(range(1000), 1000)
    ten_thous = sample(range(10000), 10000)
    hun_thous = sample(range(100000), 100000)
    for uniq2 in range(0, 100000):
        hun_vals = build_vals_tup(uniq2, hun_thous)
        insert_tuple(conn, vals=hun_vals, schema=schema, table='HUNDREDKTUP1')
        if uniq2 < 1000:
            one_vals = build_vals_tup(uniq2, one_thous)
            ten_vals = build_vals_tup(uniq2, ten_thous)
            insert_tuple(conn, vals=one_vals, schema=schema, table='ONEKTUP')
            insert_tuple(conn, vals=ten_vals, schema=schema, table='TENKTUP1')
            insert_tuple(conn, vals=ten_vals, schema=schema, table='TENKTUP2')
        elif uniq2 < 10000:
            ten_vals = build_vals_tup(uniq2, ten_thous)
            insert_tuple(conn, vals=ten_vals, schema=schema, table='TENKTUP1')
            insert_tuple(conn, vals=ten_vals, schema=schema, table='TENKTUP2')
