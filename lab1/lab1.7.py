import random
print("guess a number between 0 and 9")
x=random.randint(0,9)
y=int(input("enter number:"))
if x==y:
	print("your guess is correct")
else:
	print ("your guess is wrong")
	print("the correct answer was",x)