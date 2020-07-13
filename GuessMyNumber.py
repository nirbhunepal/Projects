from random import randint
value = randint(0, 40)
condition= True
while condition == True:
    a = int(input("Enter a Number Between 0 and 40"))
    if value>a:
        print("higher")
    elif value<a:
        print("lower")
    else:
        print("You got it right")
        condition = False