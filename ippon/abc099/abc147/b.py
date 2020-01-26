s = list(input())
ans = 0
n = len(s)-1
for i in range(len(s)):
  if s[i] != s[n-i]:
    ans += 1
print(int(ans/2))
