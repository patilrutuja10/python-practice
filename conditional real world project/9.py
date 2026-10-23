name = input("Enter customer name: ")
age = int(input("Enter age: "))
risk = input("Enter occupation risk (Low/Medium/High): ")
smoker = input("Are you a smoker? (Yes/No): ")

base_premium = 10000
additional_charges = 0

if age < 18:
    print("Customer Name:", name)
    print("Eligibility Status: Not Eligible")

else:
    if risk == "High" or risk == "high":
        additional_charges = additional_charges + 7000
    elif risk == "Medium" or risk == "medium":
        additional_charges = additional_charges + 3000

    if age > 50:
        additional_charges = additional_charges + 5000

    if smoker == "Yes" or smoker == "yes":
        additional_charges = additional_charges + 5000

    final_premium = base_premium + additional_charges

    if additional_charges >= 10000:
        message = "High Risk Policy"
    else:
        message = "Normal Risk Policy"

    print("\n--- Insurance Premium Details ---")
    print("Customer Name:", name)
    print("Eligibility Status: Eligible")
    print("Base Premium: Rs.", base_premium)
    print("Additional Charges: Rs.", additional_charges)
    print("Final Premium: Rs.", final_premium)
    print("Risk Message:", message)
