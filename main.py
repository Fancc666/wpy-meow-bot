from utils.AiConnect import AiHandler
import time

# 维护EasyConnect心跳 主函数需要要异步编写
# 但为了简化 如果需要维护心跳请独立运行 HeatBeat.py

def main():
    myHandler = AiHandler()
    print(myHandler.send_request("今天天气真好！"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[programme exit]")
