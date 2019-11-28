N = int(input())
d = list(map(int, input().split(" ")))
sum = 0
while len(d) >= 1:
    for i in range(1,len(d)):
        sum += d[0] * d[i]
    del d[0]
print(sum)
