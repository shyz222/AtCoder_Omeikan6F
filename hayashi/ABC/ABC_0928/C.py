n = int(input())
a = list(map(int, input().split(" ")))

# a.indexのところで線形探索してるっぽいので0(n**2)
# list = [a.index(x)+1 for x in range(1, n+1)]
# print(*list)

dic = {}
i = 0
for a_s in a:
    dic.setdefault(i, a_s)
    i += 1

for k in sorted(dic.items(), key=lambda x: x[1]):
    print(k + 1)
