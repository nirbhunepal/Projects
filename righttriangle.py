n = int(input("Enter A Number"))
print("the triangle will look something like this")
for i in range(1, n+1):
    for j in range(1, i+1):
        print('*', end='')
    print()
