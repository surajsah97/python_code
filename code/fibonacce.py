num = int(input("Enter number of turns You want for fibonacce >>>> "))
a=0
b=1
print(a)
for i in range(num-1):
	c=a+b
	print(c)
	b=a
	a=c