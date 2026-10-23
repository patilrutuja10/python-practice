base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
result = 1

for i in range(abs(exponent)):
    result = result * base

if exponent < 0:
    result = 1 / result

print("Answer =", result)