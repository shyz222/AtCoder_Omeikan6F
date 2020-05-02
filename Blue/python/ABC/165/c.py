import itertools
N,M,Q=map(int,input().split())
a=[0]*Q
b=[0]*Q
c=[0]*Q
d=[0]*Q

for i in range(Q):
    a[i],b[i],c[i],d[i] = map(int,input().split())
    a[i]-=1
    b[i]-=1

ans=0
for seq in itertools.combinations_with_replacement(range(M),N):
    tmp=0
    for i in range(Q):
        if seq[b[i]]-seq[a[i]]==c[i]:
            tmp+=d[i]
    ans=max(ans,tmp)

print(ans)
