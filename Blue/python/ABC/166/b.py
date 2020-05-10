N, K =map(int, input().split())
snuke = [0]*N

for i in range(K):
    d = int(input())
    a = list(map(int,input().split()))
    for j in range(d):
        snuke[a[j]-1] = 1

print(snuke.count(0))