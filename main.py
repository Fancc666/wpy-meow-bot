from utils.AiConnect import AiHandler
from utils.WpyTool import WpyHandler
from utils.EnvironTool import config
import time

# 维护EasyConnect心跳 主函数需要要异步编写
# 但为了简化 如果需要维护心跳请独立运行 HeatBeat.py

def get_time(delay=0):
    timeStamp = time.time()
    timeArray = time.localtime(timeStamp + delay)
    fmtTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return fmtTime

def main():
    print("{:*^30}".format("wpy-meow-bot"))
    print("==Author FANCC==")
    print("[programme] in service")
    print("[ai] 尝试连接ai模型")
    aiHandler = AiHandler()
    print("[ai] 连接成功")
    print("[wpy] 尝试登入微北洋")
    wpyHandler = WpyHandler()
    print("[wpy] 登入成功")
    print(f"[programme] 进入事件循环 监听#MP{config.get("WPY_POST")}")
    print(f"[programme] 循环间隔{config.get("WPY_INTERVAL")}秒 每次获取{config.get("WPY_FETCHNUM")}条")
    while True:
        print(f"[cycle] 运行时间 {get_time()}")
        # start cycle
        
        # end cycle
        print(f"[cycle] 下次运行时间 {get_time(int(config.get("WPY_INTERVAL") or 60))}")
        time.sleep(int(config.get("WPY_INTERVAL") or 60))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[programme] exit")
