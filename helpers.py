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
            db_call(cursor=cursor, *args, **kwargs)
            cursor.close()
            conn.commit()
        except pgre.DatabaseError as error:
            conn.rollback()
            print(error)
    return transaction_wrapper

@transaction
def create_schema(conn, schema, cursor=None):
    """
    Make sure to pass in a connection object! Must pass in arguments by keyword.
    Creates the named schema. Transaction decorator will pass in a 
    cursor object.
    
    Arguments:
        - conn - a postgres connection object
        - schema - name of the schema to be created
    """
    cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema};")

