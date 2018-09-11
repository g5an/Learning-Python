#enconding:utf-8
#除了数字，布尔，字符串等类型，其它类型如list要复制一个list，用切片
nums = list(range(10))
nums_tmp = nums
nums_tmp[2] = 20
print('nums=',nums)
#nums = [0, 1, 20, 3, 4, 5, 6, 7, 8, 9]  这里原序列会改变，相当于引用赋值

# 复制赋值,不会改变原有序列的值
num = list(range(10))
num_temp = num[:]
num_temp[4] = -5
print('num=',num ,'\n','num_temp=',num_temp)