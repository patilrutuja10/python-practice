name = input("Enter customer name: ")
age = int(input("Enter age: "))
show = input("Enter show type (Morning/Evening): ")
day = input("Enter day type (Weekday/Weekend): ")

price = 200
discount = 0
surcharge = 0

if age < 0:
    print("Invalid age")

else:
    if age < 12:
        discount = price * 0.50
    elif age >= 60:
        discount = price * 0.30

    if show == "Morning" or show == "morning":
        discount = discount + 30

    if day == "Weekend" or day == "weekend":
        surcharge = 50

    final_price = price - discount + surcharge

    print("\n--- Movie Ticket Details ---")
    print("Customer Name:", name)
    print("Original Ticket Price: Rs.", price)
    print("Discount: Rs.", discount)
    print("Weekend Surcharge: Rs.", surcharge)
    print("Final Ticket Price: Rs.", final_price)
