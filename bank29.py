# Banking Management System
balance = 0
def check_balance():
    print(f"\nCurrent Balance: ₹{balance}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    balance += amount
    print(f"₹{amount} deposited successfully.")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount > balance:
        print("Insufficient Balance!")
    else:
        balance -= amount
        print(f"₹{amount} withdrawn successfully.")

while True:
    print("\n===== BANKING MANAGEMENT SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        print("Thank you for using our banking system!")
        break

    else:
        print("Invalid Choice! Please try again.")