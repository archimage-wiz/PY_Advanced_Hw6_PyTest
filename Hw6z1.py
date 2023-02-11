
import requests as re
from fake_headers import Headers


class YandexDisk:

    def __init__(self, token, HOST = "https://cloud-api.yandex.net") -> None:
        self.host = HOST
        self.token = token
        self.headers = Headers(os="win", browser='opera').generate()
        self.headers['Content-Type'] = "application/json"
        self.headers["Authorization"] =  F"OAuth {self.token}"
        #print(self.headers)

    def CreateFolder(self, folder_name: str) -> int:
        req_path = "/v1/disk/resources/"
        resp = re.put(self.host + req_path, headers=self.headers, params={'path' : folder_name})
        return resp.status_code
        


def main() -> None:
    with open(".token", "r") as f:
        token = f.readline().strip()
    x = YandexDisk(token)
    x.CreateFolder("api_test/test_folder_1")
    print()


if __name__ == "__main__":
    main()