import random
arr = []
for i in range(20):
	x = int(random.random()*10)  
	arr.append(x)
	print("%3d" % x, end='')
	if (i+1) % 10 == 0:	print()
 
minimum = int(input('min: '))
maximum = int(input('max: '))
 
index = []
i = 0
for i in arr:
	if minimum <= i <= maximum:
		index.append(arr.index(i))
print("Quantity: ", len(index))
print("Indices: ", index)