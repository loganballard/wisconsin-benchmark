import psycopg2 as pgre
import argparse as argp
from os import environ as env
from helpers import get_setup_vars, generate_data, create_schema, create_tables

def cred_driver():
    """
    Collect and sets environment variables necessary for interacting
    with postgres
    """
    host = input('input the host where postgres lives: ')
    port = input('input the port postgres is listening on: ')
    db = input('input the postgres database: ')
    user = input('input the postgres username: ')
    passw = input('input the postgres password: ')
    env['P_DB'] = db
    env['P_HOST'] = host
    env['P_PORT'] = port
    env['P_USER'] = user
    env['P_PASS'] = passw

def get_connection(creds):
    """
    Given credentials and postgres info, return a posgres
    db connection
    """
    return pgre.connect(
        database = creds['db'],
        host = creds['host'],
        port = int(creds['port']),
        user = creds['user'],
        password = creds['pass']
    )

def init_database(conn):
    """
    Passing in a connection, initialize the database with
    somewhat randomized data.

    Arguments:
        - conn - postgres connection object
    """
    schema = input("Input a schema name to be created: ")
    create_schema(conn, schema)
    create_tables(conn, schema)
    generate_data(conn, schema)

def main():
    """
    Controls the user interaction with the program
    """
    parser = argp.ArgumentParser(
        description="Play around and Interact with the Wisconsin Benchmark.",
        prog="Logan's Wisconsin Benchmark"
    )
    parser.add_argument('-p', '--populate', help="populate data for the benchmark",
                    action='store_true')
    parser.add_argument('-c', '--creds', help="set environment variabes for postgres credentials",
                    action='store_true')
    args = parser.parse_args()
    if args.creds:
        cred_driver()
    creds = get_setup_vars()
    conn = get_connection(creds)
    if args.populate:
        init_database(conn)
    conn.close()

if __name__ == '__main__':
    main()