name = input("Enter customer name: ")
plan = input("Enter plan type (Basic/Standard/Premium): ")
data = float(input("Enter extra data used in GB: "))

if data < 0:
    print("Invalid data usage")

elif plan == "Basic" or plan == "basic":
    base_charge = 299
    included_data = 10

    extra_charge = data * 20
    if data > 10:
        surcharge = 100
    else:
        surcharge = 0

    total = base_charge + extra_charge + surcharge

    print("\nCustomer Name:", name)
    print("Plan Type:", plan)
    print("Base Plan Charge: Rs.", base_charge)
    print("Extra Data Charge: Rs.", extra_charge)
    print("Surcharge: Rs.", surcharge)
    print("Final Bill: Rs.", total)

elif plan == "Standard" or plan == "standard":
    base_charge = 499
    included_data = 25

    extra_charge = data * 20
    if data > 10:
        surcharge = 100
    else:
        surcharge = 0

    total = base_charge + extra_charge + surcharge

    print("\nCustomer Name:", name)
    print("Plan Type:", plan)
    print("Base Plan Charge: Rs.", base_charge)
    print("Extra Data Charge: Rs.", extra_charge)
    print("Surcharge: Rs.", surcharge)
    print("Final Bill: Rs.", total)

elif plan == "Premium" or plan == "premium":
    base_charge = 799
    included_data = 50

    extra_charge = data * 20
    if data > 10:
        surcharge = 100
    else:
        surcharge = 0

    total = base_charge + extra_charge + surcharge

    print("\nCustomer Name:", name)
    print("Plan Type:", plan)
    print("Base Plan Charge: Rs.", base_charge)
    print("Extra Data Charge: Rs.", extra_charge)
    print("Surcharge: Rs.", surcharge)
    print("Final Bill: Rs.", total)

else:
    print("Invalid plan type")
