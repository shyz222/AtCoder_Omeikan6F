import math


n = int(input())
ans_L = []
d = []
for val in range(int(math.sqrt(n)+1),0,-1):
    if n % val ==0:
        x = val
        y = int(n/val)
        #st = str(x) + "*" +str(y)
        #d.append(st) 
        #ans_L.append(int(x+y-2))
        print(int(x+y-2))
        exit()
#print(d)
#print(ans_L)
#print(min(ans_L))