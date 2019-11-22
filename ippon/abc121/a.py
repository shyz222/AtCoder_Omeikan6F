h,w = map(int,input().split())
h1,w1 = map(int,input().split())
whole = h*w

print(whole - w*h1 - abs(h-h1)*w1)
