
# Multiplication Table and Number Analyzer

# Input
num = int(input("Enter a positive integer for table: "))
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

# Multiplication table
print("\nMultiplication Table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Validate range
if start > end:
    print("\nInvalid range! Start must not be greater than end.")
else:
    even_count = 0
    odd_count = 0
    total = 0

    # Analyze numbers in range
    for i in range(start, end + 1):
        total += i

        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Display results
    print("\nEven count:", even_count)
    print("Odd count:", odd_count)
    print("Sum of range:", total)
