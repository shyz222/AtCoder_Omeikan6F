n = list(input())
s_L = list(map(int,input().split()))

s_L = list(sorted(s_L,reverse=True))
if s_L[0] < sum(s_L[1:]):
    print("Yes")
else:
    print("No")