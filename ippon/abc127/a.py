a,b = map(int,input().split())

if a >= 13:
    print(b)
elif a < 13 and a >= 6:
    print(int(b/2))
else:
    print(0)
