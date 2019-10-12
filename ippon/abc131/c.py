a,b,c,d = map(int,input().split())

ans_L = list(map(lambda x:x%6,list(range(a,b+1))))
print(len(ans_L)-ans_L.count(0))
