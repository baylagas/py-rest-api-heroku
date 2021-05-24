from core.pyba_logic import PybaLogic


class VideoLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertVideo(self, video):
        database = self.get_databaseXObj()
        sql = (
            "INSERT INTO `videoappdb`.`video` "
            + f"(`id`,`name`,`views`,`likes`) "
            + f"VALUES(0, '{video['name']}', {video['views']}, {video['likes']});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getVideoById(self, id):
        database = self.get_databaseXObj()
        sql = f"SELECT * FROM videoappdb.video where id={id};"
        result = database.executeQuery(sql)
        return result

    def updateVideo(self, id, video):
        database = self.get_databaseXObj()
        sql = (
            "UPDATE `videoappdb`.`video` "
            + f"SET `name` = '{video['name']}', `views` = {video['views']}, `likes` = {video['likes']} "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteVideo(self, id):
        database = self.get_databaseXObj()
        sql = f"DELETE FROM `videoappdb`.`video` WHERE id={id};"
        rows = database.executeNonQueryRows(sql)
        return rows
