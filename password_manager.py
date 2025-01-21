import os, time
def view():
    try:
        with open("password.txt", "r") as f:
            print("Existing passwords:")
            for line in f.readlines():
                print(line.rstrip())
    except FileNotFoundError:
        print("No existing passwords found. 'password.txt' does not exist.")
def add():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("password.txt", "a") as f:
        f.write(f"User: {username} | Password: {password}\n")
        print("Password added successfully.")   
def main():
    master_pwd = input("What is your master password? ")
    attempts = 0
    while master_pwd != "pitou":
        attempts += 1
        print("Incorrect master password. Please try again.")
        master_pwd = input("What is your master password? ")
        if attempts >= 5:
            print("Too many failed attempts. You can try after 30 seconds.")
            for i in range(30, -1, -1):
                print(f"{i}...")
                time.sleep(1)
            attempts = 0
            master_pwd = input("What is your master password? ")
    print("Master password is correct. You can now proceed.")
    os.system("cls")
    while True:
        mode = input("Would you like to add a new password or view existing passwords? (view, add) - press Q to quit: ").lower()
        if mode == "q":
            print("Exiting...")
            break
        elif mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid mode. Please enter 'view' or 'add'.")
if __name__ == "__main__":
    main()