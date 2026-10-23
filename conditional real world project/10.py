name = input("Enter customer name: ")
bill = float(input("Enter food bill amount: "))
member = input("Are you a member? (Yes/No): ")

if bill < 0:
    print("Invalid bill amount")

else:
    if bill < 1000:
        discount = 0
    elif bill < 3000:
        discount = bill * 0.05
    elif bill < 5000:
        discount = bill * 0.10
    else:
        discount = bill * 0.15

    if member == "Yes" or member == "yes":
        discount = discount + (bill * 0.05)

    amount = bill - discount
    service_charge = amount * 0.05
    final_amount = amount + service_charge

    if final_amount >= 5000:
        message = "Thank you for being a valued customer"
    else:
        message = "Thank you for visiting"

    print("\n--- Restaurant Bill ---")
    print("Customer Name:", name)
    print("Original Bill: Rs.", bill)
    print("Discount: Rs.", discount)
    print("Service Charge: Rs.", service_charge)
    print("Final Payable Amount: Rs.", final_amount)
    print("Message:", message)
