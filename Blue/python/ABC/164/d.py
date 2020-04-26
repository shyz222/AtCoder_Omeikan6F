S = input()[::-1]

cnts = [0]*2019
cnts[0] = 1
num = 0
d = 1
ans = 0

for i in S:
    num += int(i) * d
    d *= 10
    num %= 2019
    d %= 2019
    cnts[num] += 1

for j in cnts:
    ans += j * (j-1) // 2 

print(ans)