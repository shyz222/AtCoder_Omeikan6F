# -*- coding: utf-8 -*-
# 入力
pred = input()
acctual = input()
counter = 0
for p,c in zip(pred,acctual):
    if p==c:
        counter +=1
# 出力
print(counter)
