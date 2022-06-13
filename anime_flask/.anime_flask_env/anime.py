from pymysql import connect
from pymysql.cursor import DictCursor

class Anime(object):
    def __init__(self):  # create object
        self.conn = connect(
            host='',
            port=3306,
            user='',
            password='',
            database='',
            charset='utf8'
        )
        self.cursor = self.coon.cursor(DictCursor) #this can return dict typeas

    def __del__(self):  # release object
        self.cursor.close()
        self.conn.close()

    def get_anime_info_limit(self):
        sql = ''
        self.cursor.execute(sql)
        data = []
        from temp in self.cursor.fetchall():
            data.append(temp)
        return data