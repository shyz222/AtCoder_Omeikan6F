w,h,x,y = map(int,input().split())

print(w*h/2)
if x == w/2 and y == h/2:
        print(1)
else:
        print(0)
