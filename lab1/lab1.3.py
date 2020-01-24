x=str(input("enter sentence to be checked: "))
print (x)
y=len(x)
z=a=b=0
for i in x:
	if i.isalpha():
		z=z+1
	elif i.isdigit():
		a=a+1
	else:
		b=b+1
print("number of alphabets are",z)
print("and number of numbers are",a)
print("number of special characters are",b)