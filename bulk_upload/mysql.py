import json
import os
import pymysql

class mysql:
    def __load_config(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/database_config.json', mode = 'r', encoding = 'utf-8') as file:
            config = file.read()
            database_config = json.loads(config)['mysql']
            return database_config

    def insert(self, info_hash, torrent_name, torrent_contents, torrent_size):
        connection = pymysql.connect(**self.__load_config())
        cursor = connection.cursor()
        try:
            cursor.execute(
                'insert into `torrent_information_table`(`info_hash`, `torrent_name`, `torrent_contents`, `torrent_size`) values(\'{}\', \'{}\', \'{}\', \'{}\');'
                .format(info_hash, pymysql.converters.escape_string(torrent_name), pymysql.converters.escape_string(torrent_contents), torrent_size)
            )
            connection.commit()
            result = True
        except:
            result = False
            connection.rollback()
        finally:
            cursor.close()
            connection.close()
            return result

    def query_info_hash(self, info_hash):
        connection = pymysql.connect(**self.__load_config())
        cursor = connection.cursor()
        try:
            cursor.execute(
                'select * from `torrent_information_table` where `info_hash` = \'{}\';'
                .format(info_hash)
            )
            connection.commit()
            result = cursor.fetchall()
        except:
            result = False
        finally:
            cursor.close()
            connection.close()
            return result

    def query_like(self, like_string):
        connection = pymysql.connect(**self.__load_config())
        cursor = connection.cursor()
        try:
            cursor.execute(
                'select * from `torrent_information_table` where `torrent_name` like \'%{}%\';'
                .format(like_string)
            )
            connection.commit()
            result = cursor.fetchall()
        except:
            result = False
        finally:
            cursor.close()
            connection.close()
            return result