n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = list(input())

dic = {}
dic["r"] = p
dic["s"] = r
dic["p"] = s

ans = 0
counter = 0

before = ""

for i in range(n):
    if i-k > 0:
        if t[i] != t[i-k]:
            ans += dic[t[i]]
        elif i-2*k > 0 and t[i] == t[i-k] and t[i] == t[i-2*k]:
            ans += dic[t[i]]
    else:
        ans += dic[t[i]]

print(ans)
