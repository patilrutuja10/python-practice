n = int(input("Enter a number: "))

for i in range(1, abs(n) + 1):
    if n != 0 and n % i == 0:
        print(i)