from utils.AiConnect import AiHandler

def main():
    myHandler = AiHandler()
    print(myHandler.send_request("阿嚏"))

if __name__ == "__main__":
    main()
