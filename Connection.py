import psycopg2
from Config import config

def connect():
    """ Connect to the PostgreSQL database server """
    connection = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        connection = psycopg2.connect(**params)
		
        return connection
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def disconnect(connection):
    if connection is not None:
        connection.close()
        print('Database connection closed.')
    else:
        print('No connection')