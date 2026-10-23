n = int(input("Enter a number: "))
temp = abs(n)
digits = len(str(temp))
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if n >= 0 and total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")