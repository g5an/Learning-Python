#!encoding:utf-8
#交换
num = [3,8,5]
for i in range(len(num) - 1): 
    if num[i] > num[i+1]:
        tmp = num[i]
        num[i] = num[i+1]
        num[i+1] = tmp
print (num)


num2 = [3,6,1]
for j in range(len(num2) - 1): 
    if num2[j] > num2[j+1]:
        num2[j],num2[j+1] = num2[j+1],num2[j]
print (num2)