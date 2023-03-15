arr = []
n = int(input("Enter number of elements:"))
a1 = int(input("Enter first element:"))
d = int(input("Enter difference:"))

for i in (1,n + 1):
    arr.append(a1 + d * (i - 1))
print(arr)