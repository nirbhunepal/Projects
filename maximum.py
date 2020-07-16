list = [1, 5, 7, 6, 2]
highest = -1
for i in list:
    highest = i < highest
    if i > highest:
        i = highest
print("the highest number is", highest)
