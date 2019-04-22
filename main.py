import psycopg2 as pgre
import argparse as argp
from os import environ as env
from helpers import get_setup_vars, generate_data

parser = argp.ArgumentParser(
    description="Play around and Interact with the Wisconsin Benchmark.",
    prog="Logan's Wisconsin Benchmark"
)
parser.add_argument('-p', '--populate', help="populate data for the benchmark",
                   action='store_true')
parser.add_argument('-c', '--creds', help="set environment variabes for postgres credentials",
                   action='store_true')

args = parser.parse_args()

# TODO - environment variable set
# TODO - population driver