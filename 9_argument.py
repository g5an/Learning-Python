#enconding:utf-8
#position argument 位置参数
    #按照位置，依次传入参数x跟n，定义多少参数，传参时必须传入相应个数的参数
def power(x, n):
    s=1
    while n > 0:
        n = n - 1
        s = s * x
    return s
#默认参数，
    #想对于位置参数，默认参数可以简化参数的调用:注意必选参数在前。默认参数在后，否则报错
    #可以有多个默认参数
def power2(x1, n1=2):
    s1=1
    while n1 > 0:
        n1 = n1 - 1
        s1 = s1 * x1
    return s1