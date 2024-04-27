import random as r

n = int(input("Enter a range: "))
c = r.randrange(0, n)
y = int(input("Enter the number: "))
if (y == c):
    print("Congratulation the number was:", c)
else:
    print("Better luck next time.")
