import requests
from pprint import pprint


# def config_read(path):
#     filename = 'my_tokens.config'
#     contents = open(filename).read()
#     config = eval(contents)
#     YA_TOKEN = config['YA_TOKEN']
#     return YA_TOKEN

YA_TOKEN = ''   # = config_read('my_tokens.config')


class YaUploader:
    url = 'https://cloud-api.yandex.net'

    def __init__(self, ya_token):
        self.ya_token = ya_token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.ya_token)
        }

    def create_new_folder(self, dir_ya='/HW_Tests_folder'):
        """ Функция создания новой папки. """
        folder_url = self.url + '/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': dir_ya}
        response = requests.put(folder_url, headers=headers, params=params)
        return response.status_code

    def delete_folder(self, dir_ya='HW_Tests_folder'):
        """ Функция удаления новой папки. """
        folder_url = self.url + '/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': '/' + dir_ya}
        response = requests.delete(folder_url, headers=headers, params=params)
        dir_status = False
        if response.status_code == 201:
            print(f'Папка {dir_ya} на Я.Диске удалена.')
            dir_status = False
        if response.status_code == 404:
            print(f'Папки {dir_ya} на Я.Диске не существует.')
        if dir_status:
            self.folder = dir_ya
        return response.status_code

    def get_folders_list(self):
        """ Функция получения списка папок, упорядоченного по имени. """
        folder_url = self.url + '/v1/disk/resources?path=/'
        headers = self.get_headers()
        params = {'fields': '_embedded.items.name,_embedded.items.type', 'limit': 20}
        response = requests.get(folder_url, headers=headers, params=params).json()
        folders_list = []
        for folder in response['_embedded']['items']:
            folder_name = folder['name']
            folders_list.append(folder_name)
        return folders_list

    def check_folder_in_folders_list(self, dir_ya):
        folders_list = self.get_folders_list()
        if dir_ya in folders_list:
            return True
        else:
            return False

    def get_files_list(self):
        """ Функция получения списка файлов, упорядоченного по имени. """
        folder_url = self.url + '/v1/disk/resources/files'
        headers = self.get_headers()
        params = {'limit': 700}
        response = requests.get(folder_url, headers=headers, params=params).json()
        files_list = []
        for file in response['items']:
            file_name = file['name']
            files_list.append(file_name)
        return files_list

if __name__ == '__main__':
    ya_uploader = YaUploader(ya_token=YA_TOKEN)
    print(ya_uploader.create_new_folder())
    print(ya_uploader.delete_folder('HW_Tests'))
    print(ya_uploader.delete_folder('HW_'))
    pprint(ya_uploader.get_folders_list())
    print(ya_uploader.check_folder_in_folders_list('HW_Tests'))