n = int(input("Enter a number: "))
temp = n
total = 0

while temp > 0:
    digit = temp % 10
    fact = 1

    for i in range(1, digit + 1):
        fact = fact * i

    total = total + fact
    temp = temp // 10

if n >= 0 and total == n:
    print("Strong number")
else:
    print("Not a Strong number")