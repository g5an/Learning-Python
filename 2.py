#encoding:utf-8
#9X9乘法表
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