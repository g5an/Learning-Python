#encoding:utf-8
#9X9乘法表 循环 判断 print指定结尾字符
a = 1
i = 1
while a != 10 :
    if i == a :
        print ("%d X %d = %d"%(i,a,i*a))
        a = a +1 
        i = 1
        continue 
    print ("%d X %d = %d"%(i,a,i*a),end=" ")
    i = i + 1
print ('-----------------')

for row in range (1,10):
    for col in range(1,row + 1):
        print (row,'X',col,'=',row * col,end=' ')
    print()