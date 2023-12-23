import psycopg2
from configparser import ConfigParser
from Account_Type import Account_Type
from Account import Account

class Database:
    def __init__(self, filename='database.ini', section='postgresql'):
        parser = ConfigParser()
        parser.read(filename)
        self.__connection = None

        db_params = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db_params[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        
        try:
            self.__connection = psycopg2.connect(**db_params)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def disconnect(self):
        if self.__connection is not None:
            self.__connection.close()
            print('Database connection closed.')
        else:
            print('No connection')
    
    def add_account_type(self, new_name, new_description):
        if self.__connection is not None:
            cursor = self.__connection.cursor()
            new_account_type = None

            if new_name is not None and new_description is not None:
                expression = """INSERT INTO account_types(name, description)
                VALUES(%s,%s) RETURNING *;"""

                try:
                    cursor.execute(expression, (new_name, new_description))
                    new_account_type = cursor.fetchone()
                    self.__connection.commit()
                except (Exception, psycopg2.ProgrammingError) as error:
                    print(error)
            
            cursor.close()

            return new_account_type

        else:
            return 'No connection'
        
    def get_account_types(self):
        if self.__connection is not None:
            cursor = self.__connection.cursor()
            account_types = None

            try:
                expression = """SELECT * FROM account_types;"""
                cursor.execute(expression)
                account_types = cursor.fetchall()
            except (Exception, psycopg2.ProgrammingError) as error:
                print(error)

            cursor.close()

            return account_types