n=(int(input("Enter the number of N elements: ")))
num_list_1=[]
for i in range(n):
    num = int(input("Enter num "))
    num_list_1.append(num)
print(num_list_1)


m=(int(input(" Enter the number of M elements: ")))
num_list_2 = []
for i in range(m):
    num = int(input("Enter num "))
    num_list_2.append(num)
print(num_list_2)


num_list3 = num_list_1+num_list_2

print(num_list3)
for i in num_list3:
    if num_list3.count(i) > 1:
        print(i)