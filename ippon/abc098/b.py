n = int(input())
s = list(input())
ans = 0
for i in range(n):
    x = set(s[:i])
    y = set(s[i:])
    char_len = len(x & y)
    ans = max(ans,char_len)
print(ans)


