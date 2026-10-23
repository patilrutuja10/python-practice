amount=int(input("Enter the amount:"))
if amount>=3000:
    discount=amount*20/100
elif amount>=1000:
    discount=amount*10/100
else:
    discount=0
    
print("Discount=",discount)
print("final amount=",amount-discount)