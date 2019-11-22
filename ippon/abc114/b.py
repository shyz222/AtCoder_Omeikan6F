s = input()
#s = [int(i) for i in s]
#print(s)
n = 3
ans = 999999
for i in range(len(s)-n+1):
    tmp = int(s[i:i+3])
    diff = abs(tmp - 753)
    ans = min(diff,ans)
print(ans)