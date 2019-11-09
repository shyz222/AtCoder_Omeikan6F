n = int(input())
mons_L = list(map(int,input().split()))

mons_L = list(sorted(mons_L,reverse=True))

tmp = mons_L[-1]
mons_L.pop()

ans_L = []
for val in mons_L:
    mod = val % tmp
    if mod == 0:
        print(tmp)
        print("exit",val,tmp)
        exit()
    ans_L.append(mod)

print(list(sorted(ans_L,reverse=True))[0])

