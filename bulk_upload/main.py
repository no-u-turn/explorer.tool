from .control import control
from .torrent_information_parser import torrent_information_parser
import pyben
import os

entries = os.listdir('D:/torrents')
print(entries)
for i in entries:
    with open('D:/torrents/' + i, 'rb') as file:
        file_data = file.read()
        a = pyben.loads(file_data)
        spider_torrent_information_parser_messages_send = torrent_information_parser.parser(a)
        info_hash = spider_torrent_information_parser_messages_send[0]
        torrent_name = spider_torrent_information_parser_messages_send[1]
        torrent_contents = spider_torrent_information_parser_messages_send[2]
        torrent_size = spider_torrent_information_parser_messages_send[3]
        database_query_info_hash_messages = control.query_info_hash(info_hash)
        if database_query_info_hash_messages['result'] is False:
            control.insert(info_hash, torrent_name, torrent_contents, torrent_size)