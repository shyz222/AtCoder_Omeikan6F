from collections import deque

def switch(flag):
    if flag==1:
        return 2
    else:
        return 1

s = list(input())
n = int(input())


s = deque(s)

flag = 0
hanten = 1
counter = 0
for i in range(n):
    # 入力
    tmp = list(input().split())
    t = int(tmp[0])
    if len(tmp) == 3:
        f = int(tmp[1])
        c = tmp[2]
    #######################

    if t == 1:
        hanten = switch(hanten)
        counter += 1
    if t == 2:
        if (f == 1 and hanten == 1) or (f==2 and hanten==2):
            s.appendleft(c)
        if (f == 2 and hanten == 1) or (f==1 and hanten ==2):
            s.append(c)
    
if counter%2 !=0:
    s.reverse()

print("".join(s))