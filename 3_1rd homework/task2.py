a=[int(i) for i in input().split()]
b=int(input())
number=0
for i in range(len(a)):
    if (b-a[i])<b-number and b-a[i]>0:
        number=i
print(a[number])