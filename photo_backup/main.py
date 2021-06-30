from pprint import pprint
import requests
import json


with open('VK_token.txt', 'r') as file_object:
    vk_token = file_object.read().strip()
vk_id = input('Введите свой Id ВКонтакте: ')
yadisk_token = input('Введите токен с Полигона Яндекс.Диска: ')
new_folder = input('Введите имя папки Яндекс.Диска, в которую будут загружены фото: ')


class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.token = token
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version
        }
        self.owner_id = requests.get(self.url + 'users.get', self.params).json()['response'][0]['id']

    def get_photos(self, user_id=None):
        """Метод возвращает список фотографии в альбоме"""
        if user_id is None:
            user_id = self.owner_id
        photos_url = self.url + 'photos.get'
        photos_params = {
            'owner_id': user_id,
            'album_id': 'profile',
            'extended': '1',
            'count': '5',
            'photo_sizes': '1'
        }
        response = requests.get(photos_url, params={**self.params, **photos_params})
        return response.json()


vk_client = VkUser(vk_token, '5.130')
if vk_id:
    get_photos_result = vk_client.get_photos(vk_id)
else:
    get_photos_result = vk_client.get_photos()


def sorted_photos():
    """ sorted_photos -> Формирует словарь {'Кол-во лайков': 'url фото'} """
    likes_list = []
    url_list = []
    type_list = []
    for value in get_photos_result.values():
        items = value.get('items')
        for item in items:
            likes = item.get('likes')
            like = likes.get('count')
            likes_list.append(like)
            sizes = item.get('sizes')
            url = sizes[-1].get('url')
            url_list.append(url)
            size_type = sizes[-1].get('type')
            type_list.append(size_type)
            result_list = list(zip(url_list, type_list))
            photos_dict = dict(zip(likes_list, result_list))
    return photos_dict


photos_dict_sorted = sorted_photos()


def get_json():
    """ sorted_photos -> Формирует json с информацией по выгруженным фото из ВК """
    result_list = []
    for items in photos_dict_sorted.items():
        result_dict = {}
        result_dict['file_name'] = [items[0]]
        result_dict['size'] = [items[1][1]]
        result_list.append(result_dict)
    result_json = json.dumps(result_list)
    return result_json


pprint(get_json())


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, disk_file_path, file_url):
        """Метод загружает файл на яндекс диск"""
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {
            'url': file_url,
            'path': disk_file_path
        }
        response = requests.post(upload_url, headers=headers, params=params)
        return response.json()

    def get_new_folder(self):
        """Метод создает новую папку на яндекс диске"""
        up_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {
            'path': new_folder,
            'overwrite': 'true'
        }
        response = requests.put(up_url, headers=headers, params=params)
        if response.status_code != 201:
            print(f'Папка с именем "{new_folder}" уже существует!')
        else:
            print(f'Папка "{new_folder}" создана на Яндекс.Диск')

    def get_files_list(self):
        """Метод возвращает метаинформацию о папке"""
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {
            'path': f'disk:/{new_folder}',
            'limit': '5',
            'fields': '_embedded.items.name'
        }
        response = requests.get(files_url, headers=headers, params=params)
        return response.json()


if __name__ == '__main__':
    yandex_disk = YaUploader(token=yadisk_token)
    yandex_disk.get_new_folder()
    for i in photos_dict_sorted.items():
        uploader = YaUploader(token=yadisk_token)
        uploader.upload(f'{new_folder}/{i[0]}.jpg', i[1][0])
    yandex_disk = YaUploader(token=yadisk_token)
    files_list = yandex_disk.get_files_list()
    pprint(files_list)