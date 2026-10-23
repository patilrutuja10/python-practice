name = input("Enter account holder name: ")
balance = float(input("Enter current balance: "))
amount = float(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Transaction Failed: Amount must be greater than 0")

elif amount > balance:
    print("Transaction Failed: Insufficient balance")

elif amount > 20000:
    print("Transaction Failed: Maximum withdrawal is Rs. 20000")

else:
    balance = balance - amount

    print("\n--- ATM Transaction ---")
    print("Account Holder:", name)
    print("Transaction Status: Successful")
    print("Withdrawn Amount: Rs.", amount)
    print("Remaining Balance: Rs.", balance)

    if balance < 1000:
        print("Low Balance Warning")
