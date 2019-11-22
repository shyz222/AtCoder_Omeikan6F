from itertools import groupby

def all_sum(n):
    a = 0
    for val in range(n+1):
        a += val
    return a

s = list(input())

trans_L = []
yazi_L = []

for key, value in groupby(s):
    num = len(list(value))
    trans_L.append(num)
    yazi_L.append(key)

print(s)
print(trans_L)


ans = 0

for i in range(len(trans_L)):
    if i != len(trans_L)-1 and trans_L[i] == 1 and trans_L[i+1] == 1:           
        ans += 1
    elif trans_L[i] !=1:
        ans += all_sum(trans_L[i])


if trans_L[0]==1 and yazi_L[0] == ">":
    ans +=1
elif trans_L[-1] == 1 and yazi_L =="<":
    ans +=1

print(ans)