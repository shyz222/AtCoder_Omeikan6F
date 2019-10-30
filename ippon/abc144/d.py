a,b,x = map(int,input().split())
#a_L = list(map(int,input().split()))
s = a*a*b

t1 = 0
t2 = 90
state = True

while state:
    # こぼれてない
    if s > x:
        t1 = t2/2
        s = s/2
    
    # こぼれた
    elif s < x:
        t1 += t2/2 
        s = s + s/2 
    else:
        print(t2)
        exit()

    if abs(t1-t2) <= 10**(-6):
        print(t2)
        exit()