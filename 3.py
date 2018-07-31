#encoding:utf-8
#随机数小游戏
import random
random_num = random.randint(0,100)
i = 0
while i < 6:
    i = i + 1
    if i == 6:
        print("loser,try again next time")
        break
    num = int (input('please input a num rang(0,100)'))
    if num < 0 or num > 100:
        print("please input the right num")
        break
    elif num < random_num:
        print("guest small")
        continue
    elif num > random_num:
        print("guest big")
        continue
    elif num == random_num:
        print("right")
        break
       
