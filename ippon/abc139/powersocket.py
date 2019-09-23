# -*- coding: utf-8 -*-
# スペース区切りの整数の入力
tap, target = map(int, input().split(" "))

for x in range(0,target):
    y = (tap-1)*x + 1
    if y >= target:
        print(x)
        break


# 出力
#print("{} {}".format(a+b+c, s))
