import requests


class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {"Content-Type": "application/json",
                "Authorization": f"OAuth {self.token}"}

    def get_url_for_upload(self):
        name_file = path_to_file.split("\\")[-1]
        return requests.get('https://cloud-api.yandex.net:443/v1/disk/resources/upload', headers=self.get_headers(),
                            params={"path": f"/{name_file}/", "overwrite": "True"})

    def upload(self, file_path: str):
        href = self.get_url_for_upload().json().get("href")
        resp = requests.put(href, data=open(file_path, 'rb'))


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "task_1.py"
    token = "AQAAAAADVkwOAADLW9SHhDijd0GghbmAJGEwFA4"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)
