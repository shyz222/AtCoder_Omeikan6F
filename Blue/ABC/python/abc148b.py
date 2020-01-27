N = int(input())
S, T = list(input().split())
S = list(S)
T = list(T)
j = 0
for i in range(0,N+N,2):
    S.insert(i+1,T[j])
    j +=1
print("".join(S))