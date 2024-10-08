import logging
import subprocess
import mysql.connector
from tools import *


class Transaction:

    def __init__(self, connect, cursor):
        self._connect = connect
        self._cursor = cursor

    def execute(self, command, values=None):

        if values:
            self._cursor.executemany(command, values)
        else:
            self._cursor.execute(command)

    def execute_query(self, statement):

        self._connect.cmd_query(statement)

    def get_one(self):

        return self._cursor.fetchone()

    def get_many(self, size=1):

        return self._cursor.fetchmany(size)

    def get_all(self):

        return self._cursor.fetchall()

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):

        if exc_type:

            self._connect.rollback()
            if exc_type is mysql.connector.DatabaseError:
                return True
            
            logging.warning(exc_value)
            # logging.warning("transaction rollback")
            return True

        else:
            self._connect.commit()

            logging.info("transaction is committed")


class DBManager:

    def __init__(self, config):
        self._config = config
        self._connection = None
        self._cursor = None
        self._connect(config)

    def create_table(self, query):

        with Transaction(self._connection, self._cursor) as trans:
            trans.execute(query)

    def insert(self, table, columns=None, values=None):
        if columns is None:
            columns = self.get_columns(table)
        _columns = collection_to_str(columns, ", ")
        _template = collection_to_str(["%s"] * len(values[0]), ", ", False)

        with Transaction(self._connection, self._cursor) as trans:
            # print(f"INSERT INTO {wrap(table)} ({_columns}) VALUES ( {_template} );")
            trans.execute(f"INSERT INTO {wrap(table, '`')} ({_columns}) VALUES ( {_template} );", values)

    def select(self, table, columns=None):
        data = None
        with Transaction(self._connection, self._cursor) as trans:
            if columns is None:
                trans.execute(f"SELECT * FROM {wrap(table, '`')};")
            else:
                trans.execute(f"SELECT {collection_to_str(columns, ', ')} FROM {wrap(table, '`')}")
            data = trans.get_all()

        return data

    def update(self, table, columns, values):
        self.delete(table)
        self.insert(table, columns, values)

    def delete(self, table):

        with Transaction(self._connection, self._cursor) as trans:
            trans.execute(f"DELETE FROM {wrap(table, '`')};")

    def default_auto_increment(self, table, value=1):
        with Transaction(self._connection, self._cursor) as trans:
            trans.execute(f"alter table {wrap(table, '`')} auto_increment = {value};")

    def get_columns(self, table):
        data = None
        with Transaction(self._connection, self._cursor) as trans:
            trans.execute(f"show columns from {wrap(table, '`')};")
            data = trans.get_all()

        return [column[0] for column in data]

    def __switch_db(self, connection, config):

        with Transaction(connection, None) as trans:
            trans.execute_query(f"CREATE DATABASE {wrap(config['database'], '`')};")

        connection.database = config["database"]

    def dump(self, dump_name="main.sql"):

        try:
            cmd = f"mysqldump -h {self._config['host']} -u {self._config['user']} -p {self._config['database']} > {dump_name}"
            subprocess.run(cmd, shell=True)
        except:
            ...

    def restore(self, dump_name="main.sql"):

        try:
            cmd = f"mysql -h {self._config['host']} -u {self._config['user']} -p {self._config['database']} < {dump_name}"
            subprocess.run(cmd, shell=True)
        except:
            ...

    def get_size_table(self, table):

        with Transaction(self._connection, self._cursor) as trans:
            trans.execute(f"""
            SELECT
            table_name AS `Table`,
            round(((data_length + index_length) / 1024 ), 2) `Size in KB`
            FROM information_schema.TABLES
            WHERE table_schema = {self._config["database"]}
            AND table_name = {wrap(table)};
            """)

    def get_size_tables(self):

        with Transaction(self._connection, self._cursor) as trans:
            trans.execute(f"""
            SELECT
            table_name AS `Table`,
            round(((data_length + index_length) / 1024 ), 2) `Size in KB`
            FROM information_schema.TABLES
            WHERE table_schema = {self._config["database"]};
            """)

    def get_average_table_size(self):

        with Transaction(self._connection, self._cursor) as trans:
            trans.execute(f"""
            SELECT round(sum((data_length + index_length) / 1024 ), 2) / count(*)  `Size in KB`
            FROM information_schema.TABLES
            WHERE table_schema = {wrap(self._config["database"])} group by table_schema
            """)
            return trans.get_one()

    def get_size_databases(self):

        with Transaction(self._connection, self._cursor) as trans:
            trans.execute(f"""
            SELECT table_schema "DB Name",
            ROUND(SUM(data_length + index_length) / 1024 / 1024, 1) "DB Size in MB" 
            FROM information_schema.tables 
            GROUP BY table_schema;
            """)

    def get_size_database(self):
        
        with Transaction(self._connection, self._cursor) as trans:
            trans.execute(f"""
            SELECT 
            ROUND(SUM(data_length + index_length) / 1024 / 1024, 1) "DB Size in MB" 
            FROM information_schema.tables WHERE table_schema = {wrap(self._config["database"])}
            GROUP BY table_schema ;
            """)
            return trans.get_one()

    def _connect(self, config):

        self._connection = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"]
        )

        self.__switch_db(self._connection, config)

        self._cursor = self._connection.cursor()

    def switch_database(self, name_db):

        self._config["database"] = name_db

        self._disconnect()

        self._connect(self._config)

        self._cursor = self._connection.cursor()

    def _disconnect(self):

        self._cursor.close()
        self._connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):

        self._disconnect()
