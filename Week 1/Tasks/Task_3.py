num = [20,15,185,100,56]
largest = num[0]
sec_largest = num[0]
for i in range(len(num)):
    if num[i] > largest:
        largest = num[i]
for i in range(len(num)):
    if (num[i]>sec_largest and num[i]!= largest):
        sec_largest = num[i]
print("Second Largest = ", sec_largest)