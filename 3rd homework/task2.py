n = int(input())
a = list(map(int, input().split()))
x = 0
i = 1
for i in range (n):
    if (a[i]+a[i+1]+a[i-1] > x):
        x = a[i]+a[i+1]+a[i-1]
print(x)