n = int(input("Enter a Number"))
total= 0
counter= 0
while (n != 0):
    remainder = n%10
    if(counter%2 == 0):
        total= total+remainder
    n=(int) (n/10)
    counter=counter+1
print("The Total is", total)
