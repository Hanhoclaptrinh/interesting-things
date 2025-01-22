import random, time, os, platform

# số dư ban đầu
balance = 10_000_000

# xóa màn hình
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# hiển thị bảng trò chơi
def display_menu():
    print("========== Lucky Draw ==========")
    print("Items: 🍒 🍉 🍋 🔔 ⭐")
    print("=================================")
    print(f"Số tiền còn lại: {balance:,} VNĐ")

# quay ngẫu nhiên vật phẩm
def draw_item():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]

# hiển thị vật phẩm sau khi quay
def print_item(row):
    clear_screen()
    print("=================================")
    print("Kết quả: " + " | ".join(row))
    print("=================================")

# tiền thưởng
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 5
        elif row[0] == '🍋':
            return bet * 10
        elif row[0] == '🔔':
            return bet * 20
        elif row[0] == '⭐':
            return bet * 50
    return 0

# quay (có animations)
def spin():
    spinner = ['🍒', '🍉', '🍋', '🔔', '⭐']
    for _ in range(10):
        print("Đang quay...", " | ".join(random.choices(spinner, k=3)), end="\r")
        time.sleep(0.2)
    print()

def main():
    global balance
    while True:
        if balance <= 0:
            print("Số dư không đủ để tiếp tục trò chơi!")
            choice = input("Bạn có muốn nạp thêm tiền vào tài khoản? (y/n): ").lower().strip()
            if choice == 'y':
                try:
                    deposit = int(input("Nhập số tiền bạn muốn nạp: ").strip())
                    if deposit > 0:
                        balance += deposit
                        print(f"Bạn đã nạp {deposit:,} VNĐ vào tài khoản.")
                    else:
                        print("Số tiền nạp phải lớn hơn 0!")
                except ValueError:
                    print("Vui lòng nhập một số hợp lệ!")
                continue
            else:
                print("Cảm ơn bạn đã tham gia trò chơi! Hẹn gặp lại bạn trong lần chơi tiếp theo!")
                break
            
        display_menu()
        
        try:
            bet = int(input("Nhập số tiền đặt cược: ").strip())
        except ValueError:
            print("Vui lòng nhập một số hợp lệ!")
            continue

        if bet > balance:
            print("Số tiền đặt cược không đủ!")
            continue
        if bet <= 0:
            print("Vui lòng đặt cược lớn hơn 0!")
            continue

        spin()
        balance -= bet
        row = draw_item()
        print_item(row)

        payout = get_payout(row, bet)
        if payout > 0:
            balance += payout
            print(f"Chúc mừng! Bạn đã trúng thưởng {payout:,} VNĐ!")
        else:
            print("Chúc bạn may mắn lần sau!")
        print()

if __name__ == "__main__":
    main()