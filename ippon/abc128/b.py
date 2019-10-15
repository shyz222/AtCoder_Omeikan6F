n = int(input())
list = []

for i in range(n):
    s, p = map(str, input().split())
    list.append([s, int(p), i+1])

list.sort(key=lambda x:x[1], reverse=True)
list.sort(key=lambda x:x[0])
for val in list:
    print(val[2])
