n = int(input("Enter a Number"))
list = []
Found = True
while Found == True:
    Found = False
    for i in range(2, n-1):
        if n % i == 0:
            list.append(i)
            n = int (n/i)
            Found = True
            break
list.append(n)

a = int(input("Enter Another Number"))
list2 = []
Found = True
while Found == True:
    Found = False
    for i in range(2, a-1):
        if a % i == 0:
            list2.append(i)
            a = int(a/i)
            Found = True
            break
list2.append(a)



gcflist = []
lcmlist = []

index1 = 0
index2 = 0
while (index1 < len(list) and index2 < len(list2)):

    if list[index1] == list2[index2]:
        gcflist.append(list[index1])
        lcmlist.append(list[index1])
        index1 = index1+1
        index2 = index2 + 1
    elif list[index1] > list2[index2]:
        lcmlist.append(list2[index2])
        index2 = index2+1
    else:
        lcmlist.append(list[index1])
        index1 = index1+1


while (index1 < len(list)):
    lcmlist.append(list[index1])
    index1 = index1+1

while (index2 < len(list2)):
    lcmlist.append(list2[index2])
    index2 = index2+1

lcm = 1
for i in lcmlist:
    lcm = lcm*i
print("The LCM of these 2 numbers is", lcm)

gcf = 1
for i in gcflist:
    gcf = gcf*i
print("The GCF of these 2 numbers is", gcf)
