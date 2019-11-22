N,Q = map(int,input().split())
s = input()

t = [0] * (N +1)


for i in range(N):
    t[i+1] = t[i] + (1 if s[i:i+2]=="AC" else 0)

print(t)

for i in range(Q):
    l, r = map(int, input().split())
    print(t[r-1] - t[l-1])