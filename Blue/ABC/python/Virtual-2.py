s = str(input().split())
ans = 0
for i in range(len(s)):
    if s[i] == "1":
        ans += 1
    else: ans += 0
    
print(ans)