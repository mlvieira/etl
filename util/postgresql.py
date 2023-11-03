import psycopg2
from psycopg2.extras import execute_batch
import pandas as pd

class PostgreSQL(object):

    def __init__(self, postgre_config):
        self.cursor = None
        self.connection = None
        self.postgre_config = postgre_config
        self.connect()
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.postgre_config['host'],
                port=self.postgre_config['port'],
                database=self.postgre_config['database'],
                user=self.postgre_config['user'],
                password=self.postgre_config['password']
            )
            self.open_cursor()
        except psycopg2.Error as e:
            pint(f"{type(e).__module__.removesuffix('.errors')}:{type(e).__name__}: {str(e).rstrip()}")


    def insert_list(self, str_consulta, obj_list = []):
        self.check_conn()

        execute_batch(self.cursor, str_consulta, obj_list, page_size=1000)

        self.commit()


    def check_conn(self):
        if self.connection is None:
            print('conectando')
            self.connect()
            self.open_cursor()


    def open_cursor(self):
        self.cursor = self.connection.cursor()


    def execute_cursor(self, str_consulta):
        self.cursor.execute(str_consulta)


    def close_cursor(self):
        self.cursor.close()


    def close_connection(self):
        self.connection.close()


    def commit(self):
        self.connection.commit()


    def execute(self, str_consulta):
        self.check_conn()

        self.execute_cursor(str_consulta)

        self.commit()


    def truncate_table(self, table_name: str, table_owner: str):
        self.check_conn()

        self.execute('TRUNCATE TABLE %s.%s' % (table_owner, table_name))


    def drop_table(self, table_name: str, table_owner: str):
        self.check_conn()

        self.execute('DROP TABLE %s.%s' % (table_owner, table_name))


    def create_staging_table(self, table_name: str, ddl: str) -> None:
        self.check_conn()

        try:
            self.execute(ddl)
        except psycopg2.Error as e:
            pint(f"{type(e).__module__.removesuffix('.errors')}:{type(e).__name__}: {str(e).rstrip()}")

    def return_as_dataframe(self, str_consulta, columns):

        self.execute_cursor(str_consulta)

        return pd.DataFrame(self.cursor.fetchall(), columns=columns)


        