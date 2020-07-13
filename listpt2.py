list = [2, 5, 8, 7, 3, 5, 1,2,3]
sum = 0
counter= 0
for i in list:
    counter = counter+1
    sum = i+sum
    if counter%3 == 0:
        print(sum)
        sum= 0