n = int(input("Enter the first number"))
m = int(input("Enter the second number"))
remainder = 1
while remainder > 0:
    remainder = n % m
    n = m
    m = remainder
print("the GCF of these two numbers is", n)
