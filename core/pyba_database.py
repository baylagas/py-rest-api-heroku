import pymysql


class PybaDatabase:
    def __init__(self):
        self.__host = "us-cdbr-east-02.cleardb.com"
        self.__port = 3306
        self.__user = "bc39f2aaa489b1"
        self.__passwd = "858e3286"
        self.__database = "heroku_312c6ee9a721c2c"
        self.__connection = self.__createConnection()
        self.__cursor = self.__createCursor()

    def get_host(self):
        return self.__host

    def get_port(self):
        return self.__port

    def get_user(self):
        return self.__user

    def __get_password(self):
        return self.__passwd

    def get_database(self):
        return self.__database

    def __get_connection(self):
        return self.__connection

    def __get_cursor(self):
        return self.__cursor

    def __createConnection(self):
        con = pymysql.connect(
            host=self.get_host(),
            port=self.get_port(),
            user=self.get_user(),
            passwd=self.__get_password(),
            database=self.get_database(),
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
        return con

    def __createCursor(self):
        con = self.__get_connection()
        cursor = None
        if con is not None:
            cursor = con.cursor()
        else:
            print("app is disconnected from database")
        return cursor

    def executeQuery(self, sql):
        cursor = self.__get_cursor()
        result = None
        if cursor is not None:
            cursor.execute(sql)
            result = cursor.fetchall()
        return result

    def executeNonQueryBool(self, sql):
        cursor = self.__get_cursor()
        con = self.__get_connection()
        hasAffected = False
        if cursor is not None:
            cursor.execute(sql)
            con.commit()
            rows = cursor.rowcount
            if rows > 0:
                hasAffected = True
        return hasAffected

    def executeNonQueryRows(self, sql):
        cursor = self.__get_cursor()
        con = self.__get_connection()
        rows = 0
        if cursor is not None:
            cursor.execute(sql)
            con.commit()
            rows = cursor.rowcount
        return rows
