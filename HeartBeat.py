import time
import requests
from utils.EnvironTool import config

def heart_beat():
    sl = int(config.get("HB_INTERVAL") or 60)
    print(f"[heart beat] started with interval {sl}s")
    while True:
        try:
            response = requests.get("https://ai.tju.edu.cn/", timeout=2)
        except requests.exceptions.Timeout:
            print("请检查网络环境")
            break
        print(f"[heart beat] fetched {response.status_code}")
        if response.status_code != 200:
            print("[heart beat] 请检查网络环境")
        time.sleep(sl)

if __name__ == "__main__":
    try:
        print("[heart beat] start")
        heart_beat()
    except KeyboardInterrupt:
        print("[heart beat] exit")
