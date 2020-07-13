n = int(input("Enter a Number"))
isPrime = True
for i in range(2, n):
    if n%i == 0:
        isPrime = False
        break
if isPrime == False:
    print("This is not prime number")
else:
    print("this is a prime number")
