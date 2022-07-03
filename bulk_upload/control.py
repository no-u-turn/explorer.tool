from mysql import mysql
import json
import os
import time

class control:
    def insert(self, info_hash, torrent_name, torrent_contents, torrent_size):
        try:
            torrent_contents = json.dumps(torrent_contents)
            with open(os.path.dirname(os.path.abspath(__file__)) + '/database_config.json', mode = 'r', encoding = 'utf-8') as file:
                config = file.read()
                default_database = json.loads(config)['default_database']
                if default_database == 'mysql':
                    result = mysql().insert(info_hash, torrent_name, torrent_contents, torrent_size)
                    return_data = {
                        'result': result,
                        'header': {
                            'info_hash': info_hash,
                            'torrent_name': torrent_name,
                            'torrent_contents': torrent_contents,
                            'torrent_size': torrent_size
                        }
                    }
                    return return_data
        except:
            return_data = {
                'result': False,
                'header': {
                    'info_hash': info_hash,
                    'torrent_name': torrent_name,
                    'torrent_contents': torrent_contents,
                    'torrent_size': torrent_size
                }
            }
            return return_data

    def query_info_hash(self, info_hash):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/database_config.json', mode = 'r', encoding = 'utf-8') as file:
            config = file.read()
            default_database = json.loads(config)['default_database']
            if default_database == 'mysql':
                result = mysql().query_info_hash(info_hash)
                if result is False:
                    return_data = {
                        'result': False,
                        'header': {
                            'info_hash': info_hash
                        }
                    }
                    return return_data
                elif len(result) > 0:
                    data = {}
                    for i in range(0, len(result)):
                        data.update({str(i): {}})
                        data[str(i)]['info_hash'] = result[i][1]
                        data[str(i)]['torrent_name'] = result[i][2]
                        torrent_contents = json.loads(result[i][3])
                        data[str(i)]['torrent_contents'] = torrent_contents
                        data[str(i)]['torrent_size'] = result[i][4]
                        discovered_on = result[i][5].timetuple()
                        discovered_on = time.mktime(discovered_on)
                        discovered_on = int(discovered_on)
                        data[str(i)]['discovered_on'] = discovered_on
                    return_data = {
                        'result': data,
                        'header': {
                            'info_hash': info_hash
                        }
                    }
                    return return_data
                else:
                    return_data = {
                        'result': False,
                        'header':
                        {
                            'info_hash': info_hash
                        }
                    }
                    return return_data

    def query_like(self, like_string):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/database_config.json', mode = 'r', encoding = 'utf-8') as file:
            config = file.read()
            default_database = json.loads(config)['default_database']
            if default_database == 'mysql':
                result = mysql().query_like(like_string)
                if result is False:
                    return_data = {
                        'result': False,
                        'header': {
                            'like_string': like_string
                        }
                    }
                    return return_data
                elif len(result) > 0:
                    data = {}
                    for i in range(0, len(result)):
                        data.update({str(i): {}})
                        data[str(i)]['info_hash'] = result[i][1]
                        data[str(i)]['torrent_name'] = result[i][2]
                        torrent_contents = json.loads(result[i][3])
                        data[str(i)]['torrent_contents'] = torrent_contents
                        data[str(i)]['torrent_size'] = result[i][4]
                        discovered_on = result[i][5].timetuple()
                        discovered_on = time.mktime(discovered_on)
                        discovered_on = int(discovered_on)
                        data[str(i)]['discovered_on'] = discovered_on
                    return_data = {
                        'result': data,
                        'header': {
                            'like_string': like_string
                        }
                    }
                    return return_data
                else:
                    return_data = {
                        'result': False,
                        'header': {
                            'like_string': like_string
                        }
                    }
                    return return_data