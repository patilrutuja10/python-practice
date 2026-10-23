total = 0

while True:
    n = int(input("Enter a number (0 to stop): "))

    if n == 0:
        break

    total = total + n

print("Sum =", total)