while True:
    amount= int(input())
    if amount%100 ==0:
        print(f"Withdrawal of {amount} is successful!")
        break
    else:
        print("Invalid amount . Please enter a multiple of 100.")