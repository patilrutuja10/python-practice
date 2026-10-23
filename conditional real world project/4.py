name = input("Enter student name: ")
percentage = float(input("Enter percentage: "))
income = float(input("Enter annual family income: "))
attendance = float(input("Enter attendance percentage: "))

if percentage >= 75 and income <= 400000 and attendance >= 75:

    if percentage >= 90:
        print("Student Name:", name)
        print("Eligibility Status: Eligible")
        print("Scholarship Category: Full Scholarship")
    else:
        print("Student Name:", name)
        print("Eligibility Status: Eligible")
        print("Scholarship Category: Partial Scholarship")

else:
    print("Student Name:", name)
    print("Eligibility Status: Not Eligible")
    print("Scholarship Category: None")

    if percentage < 75:
        print("Reason: Percentage is below 75%")
    elif income > 400000:
        print("Reason: Family income is above Rs. 4,00,000")
    elif attendance < 75:
        print("Reason: Attendance is below 75%")
