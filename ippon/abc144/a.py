a,b = map(int,input().split())
#a_L = list(map(int,input().split()))
 
if a >= 10 or b >= 10:
    print(-1)
else:
    print(a*b)