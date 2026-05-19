from utils.AiConnect import AiHandler

def main():
    myHandler = AiHandler()
    print(myHandler._send_request("你好"))

if __name__ == "__main__":
    main()
