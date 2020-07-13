n = int(input("Enter Number of Rows"))
print("The diamond will look like this")
for i in range(1, n+1):
    for k in range(1, n-i+1):
        print(' ', end='')
    for j in range(1, i*2):
        print('*', end='')
    print()
for i in range(1, n):
    for k in range(1, i+1):
        print(' ', end='')
    for j in range(1, (n-i)*2):
        print('*', end='')
    print()
