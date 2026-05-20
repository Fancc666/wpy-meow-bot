from urllib.parse import urlencode
import requests
import json
from utils.EnvironTool import config
from utils.SeenHandler import get_new_replys

class WpyHandler:
    def __init__(self) -> None:
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
        }
        self.token = ""
        self.session = requests.session()
        self.get_token()
    def get_token(self):
        auth = self.session.get(
            "https://qnhd.twt.edu.cn/api/v1/f/auth/passwd?" + urlencode({
                "user": config.get("WPY_USER"),
                "password": config.get("WPY_PASSWD")
            }),
            headers=self.headers
        )
        # print(auth.text)
        assert auth.status_code == 200, "请求错误"
        auth = json.loads(auth.text)
        assert auth.get("code") == 200, "认证错误"
        self.token = auth["data"]["token"]
        self.headers.update({
            "token": auth["data"]["token"]
        })
    def get_replys(self):
        replys = self.session.get(
            "https://qnhd.twt.edu.cn/api/v1/f/floors?" + urlencode({
                "post_id": config.get("WPY_POST"),
                "page_size": config.get("WPY_FETCHNUM")
            }),
            headers=self.headers
        )
        assert replys.status_code == 200, "请求错误"
        replys = json.loads(replys.text)
        assert replys.get("code") == 200, "获得floors错误"
        return replys["data"]["list"]
    def get_new_floors(self):
        news = get_new_replys(self.get_replys())
        print(f"[floors] #MP{config.get("WPY_POST")}发现新回复{len(news)}条")
        print(f"[floors] id -> {[k["id"] for k in news]}")
        return news
    def reply_to_floor(self, floor, text):
        response = self.session.post(
            "https://qnhd.twt.edu.cn/api/v1/f/floor/reply",
            data={
                "reply_to_floor": floor,
                "content": text,
                "images": ""
            },
            headers=self.headers
        )
        print(response.text)
        assert response.status_code == 200, "请求错误"
        response = json.loads(response.text)
        if response.get("code") != 200:
            raise Exception(response["data"]["error"])
        print("[reply] 回复成功")
