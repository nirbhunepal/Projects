letters = ["n", "a", "b", "n"]
n = len(letters)
condition = True
for i in range(n):
    if letters[i] == letters[n - i - 1]:
        condition = True
    else:
        condition = False
        break

if condition is True:
    print("This is a palindrome")
else:
    print("This is not a palindrome")
