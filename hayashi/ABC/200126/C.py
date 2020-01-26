H, K = map(int, input().split())

list = list(map(int,list(input().split())))
ld = sorted(list, reverse=True)
print(sum(ld[K:]))
