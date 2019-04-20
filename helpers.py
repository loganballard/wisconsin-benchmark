import psycopg2
from os import environ as env

def get_setup_vars():
    return {
        'db': env['P_DB'] if env.get('P_DB') else 'postgres',
        'host': env['P_HOST'] if env.get('P_HOST') else 'localhost',
        'port': env['P_PORT'] if env.get('P_PORT') else 5342,
        'user': env['P_USER'] if env.get('P_USER') else 'admin',
        'pass': env['P_PASS'] if env.get('P_PASS') else 'admin'
    }

