from control import control
from torrent_information_parser import torrent_information_parser
import pyben
import PySimpleGUI
import os

torrent_file_folder_path = PySimpleGUI.popup_get_folder('bulk upload')
if not torrent_file_folder_path == None:
    if os.path.exists(torrent_file_folder_path):
        files_name = os.listdir(torrent_file_folder_path)
        for i in files_name:
            if i.endswith('.torrent') is True:
                with open(torrent_file_folder_path + '/' + i, 'rb') as file:
                    file_data = file.read()
                    torrent_data = pyben.loads(file_data)
                    torrent_information_parser_messages = torrent_information_parser().parser(torrent_data)
                    if torrent_information_parser_messages is not False:
                        info_hash = torrent_information_parser_messages[0]
                        torrent_name = torrent_information_parser_messages[1]
                        torrent_contents = torrent_information_parser_messages[2]
                        torrent_size = torrent_information_parser_messages[3]
                        database_query_info_hash_messages = control().query_info_hash(info_hash)
                        if database_query_info_hash_messages['result'] is False:
                            control().insert(info_hash, torrent_name, torrent_contents, torrent_size)
        PySimpleGUI.popup('upload success')
    else:
        PySimpleGUI.popup('upload failure')