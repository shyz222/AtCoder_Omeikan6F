n = int(input())
#a = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(int(input()))

b=sorted(a,reverse=True)
max_a=b[0]
max_a2=b[1]

for i in range(n):
    if a[i]==max_a:
        print(max_a2)
    else:
        print(max_a)
