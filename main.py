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
    isFirstCycle = True
    while True:
        print(f"\033[32m[cycle]\033[0m 运行时间 {get_time()}")
        # start cycle
        print(f"[cycle] 获取新回复")
        newFloors = wpyHandler.get_new_floors()
        if len(newFloors) == 0:
            print(f"[main] 本轮没有检测到新回复")
        for floor in newFloors:
            print("*"*30)
            print(f"[main] 处理回复id {floor["id"]}")
            print(f"[main] 用户回复 {floor["content"]}")
            if floor["content"] == "":
                print(f"[skip] 空回复")
                continue
            if isFirstCycle:
                print(f"[main] 首轮循环不回复")
            else:
                print(f"[main] 调用AI模型生成回复")
                aiReply = aiHandler.send_request(floor["content"])
                print(f"[main] AI回复 {aiReply}")
                if config.get("DEBUG_MODE") == "true":
                    print(f"[main] DEBUG_MODE未发送到微北洋")
                else:
                    wpyHandler.reply_to_floor(floor["id"], aiReply)
            print("*"*30)
            time.sleep(1) # 防止调用过快
        # end cycle
        print(f"[cycle] 下次运行时间 {get_time(int(config.get("WPY_INTERVAL") or 60))}")
        isFirstCycle = False
        time.sleep(int(config.get("WPY_INTERVAL") or 60))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[programme] exit")
