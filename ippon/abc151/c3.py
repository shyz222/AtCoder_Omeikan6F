N,M = map(int,input().split())
PS = []
for i in range(M):
    p,s = map(str,input().split())
    PS.append((p,s))
 
AC = [False] * (N+1)
WA_cnt = [0] * (N+1)
 
penal = 0
for p,s in PS:
    #print(p,s)
    p = int(p)
    if AC[p]:
        continue
    if s == b'WA':
        WA_cnt[p] += 1
    else:
        AC[p] = True
        penal += WA_cnt[p]
print(AC)
ac = sum(AC)
print(ac, penal)
