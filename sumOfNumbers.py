n=int(input("enter a number"))
total=0
for m in range (1, n+1):
    if(m%2 !=0):
        total=total+m
print("the sum of", n ,"numbers is", total)