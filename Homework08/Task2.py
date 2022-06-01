import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str, file_name):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        params = {'path': f'Netology/{file_name}', 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)

        href = response.json().get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Файл загружен")
        else:
            print("Файл не загружен")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    file_list = ['newsafr.xml', 'newsafr.json']
    token = '___'

    """В методе Upload указано, что он загружает файлы по списку file_list"""
    for name in file_list:
        path_to_file = os.path.join(os.getcwd(), 'quiz', name)
        uploader = YaUploader(token)
        result = uploader.upload(path_to_file, name)

