list = ["this", "is", "a", "Sentence", "waters"]
counter = 0
for item in list:
    n= len(item)
    if (n % 2)== 0:
        counter=counter+1
print("the number of items in this list is", counter)
