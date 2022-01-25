import mysql.connector as mysql

#class for data connectivity with MySql
class DatabaseConnection(object):
    def __new__(cls, *args, **kwargs):
        conn = mysql.connect(
            host='127.0.0.1',
            database='villagecouncil',
            user='rushi',
            password='Rushi_1192#'
        )
        print(type(conn))
        return conn

    def __del__(self):
        self.conn.close()

#functions for convertiting functions
class ConvertFunction(object):
    pass
