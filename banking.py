def depos(a, b):
    return a + b
    
def withdrw(a, b):
    return a - b




menu = {
    1: {"Account": "User1", "Balance": "5,000", "Action": [depos, withdrw], "History": "X", "PIN": "4334", "Locked": False},
    2: {"Account": "User2", "Balance": "3,450", "Action": [depos, withdrw], "History": "X", "PIN": "5112", "Locked": False},
    3: {"Account": "User3", "Balance": "10,000", "Action": [depos, withdrw], "History": "X", "PIN": "5141", "Locked": False}
}


def actions(menu_id):
    choices = menu[menu_id]

    if choices["Locked"]:
        print("Locked.")
        return

    retries = 3
    while retries > 0:
        pin = input("Please enter your bank PIN:")
        if pin == choices["PIN"]:
            print(f"You currently have: {choices['Balance']}")
            while True:
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Return to menu.")
                print("4. Continue")
                choice = input("Choose: ")
                if choice == "1":
                    balance_str = choices["Balance"].replace(",", "")
                    current_balance = float(balance_str)
                    deposit_amount = float(input("Enter amount to deposit: "))
                    if deposit_amount < 0:
                        print("Cannot deposit negative amount.")
                        continue
                    result = depos(current_balance, deposit_amount)
                    print(f"New balance: {result}")
                elif choice == "2":
                    balance_str = choices["Balance"].replace(",", "")
                    current_balance = float(balance_str)
                    withdraw_amount = float(input("Enter amount to withdraw: "))
                    if withdraw_amount > current_balance:
                        print("Cannot overdraft, please try again.")
                        continue
                    result = withdrw(current_balance, withdraw_amount)
                    print(f"New balance: {result}")
                elif choice == "4":
                    continue
                elif choice == "3":
                    return
        else:
            retries -= 1
            print(f"Incorrect PIN, you have {retries} left")
    if retries == 0:
        choices["Locked"] = True
        print("Retries used up, returning to menu...")
        return
    





loop = True
while loop:
    print("==PYTHON BANK==")
    for menu_id, data in menu.items():
        print(f"{menu_id}. {data['Account']}")
    try:
        choice = int(input("Please select an option(1-4): "))
    except ValueError:
        print("Invalid input.")
        continue

    if choice == 4:
        print("Thank you for operating with us.")
        loop = False
    elif choice in menu:
        actions(choice)
    else:
        print("Invalid input.")

        