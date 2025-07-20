def add():
    name = input("Account Name: ")
    pasw = input("Password: ")

    with open("PasswordList.txt", "a") as f:
        f.write(f"Username: {name}\nPassword: {pasw}\n\n")
    print("Password saved successfully!")


def view():
    with open("PasswordList.txt", "r") as f:
        print(f.read())


if __name__ == "__main__":
    print("PASSWORD MANAGER")

    master_pass = "mariA000"
    ask = input("What is the master password? ")
    while ask != master_pass:
        print("Wrong master key")
        continue

    while True:
        print("1. Add Password")
        print("2. View Password")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError as e:
            print(e)
            continue

        if choice == 1:
            add()
        elif choice == 2:
            view()
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
