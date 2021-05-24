from core.pyba_database import PybaDatabase


class PybaLogic:
    def __init__(self):
        self.__databaseXObj = self.__createDatabaseX()

    def get_databaseXObj(self):
        return self.__databaseXObj

    def __createDatabaseX(self):
        database = PybaDatabase()
        return database
