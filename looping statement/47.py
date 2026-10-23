n = abs(int(input("Enter a number: ")))
product = 1

if n == 0:
    product = 0
else:
    while n > 0:
        digit = n % 10
        product = product * digit
        n = n // 10

print("Product of digits =", product)