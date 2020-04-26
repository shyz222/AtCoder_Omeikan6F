#n = int(input())
#L = list(map(int,input().split()))
s = list(input())


s_r = []
for val in range(len(s)-1,-1,-1):
    s_r.append(s[val])

ans = 0
#print(s_r)
#wrong = []
for val in range(len(s)):
    if s[val] != s_r[val]:
        ans += 1

    #print(s[val],s_r[val])

print(ans)
