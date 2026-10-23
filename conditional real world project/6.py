name = input("Enter guest name: ")
room = input("Enter room type (Standard/Deluxe/Suite): ")
nights = int(input("Enter number of nights: "))

if nights <= 0:
    print("Error: Number of nights must be greater than 0")

elif room == "Standard" or room == "standard":
    price = 2000
    charge = price * nights

    if nights >= 10:
        discount = charge * 0.20
    elif nights >= 5:
        discount = charge * 0.10
    else:
        discount = 0

    final_amount = charge - discount
    print("\nGuest Name:", name)
    print("Room Type:", room)
    print("Number of Nights:", nights)
    print("Room Charge: Rs.", charge)
    print("Discount: Rs.", discount)
    print("Final Booking Amount: Rs.", final_amount)

elif room == "Deluxe" or room == "deluxe":
    price = 3500
    charge = price * nights

    if nights >= 10:
        discount = charge * 0.20
    elif nights >= 5:
        discount = charge * 0.10
    else:
        discount = 0

    final_amount = charge - discount
    print("\nGuest Name:", name)
    print("Room Type:", room)
    print("Number of Nights:", nights)
    print("Room Charge: Rs.", charge)
    print("Discount: Rs.", discount)
    print("Final Booking Amount: Rs.", final_amount)

elif room == "Suite" or room == "suite":
    price = 6000
    charge = price * nights

    if nights >= 10:
        discount = charge * 0.20
    elif nights >= 5:
        discount = charge * 0.10
    else:
        discount = 0

    final_amount = charge - discount
    print("\nGuest Name:", name)
    print("Room Type:", room)
    print("Number of Nights:", nights)
    print("Room Charge: Rs.", charge)
    print("Discount: Rs.", discount)
    print("Final Booking Amount: Rs.", final_amount)

else:
    print("Error: Invalid room type")
