a, b, m = map(int, input().split())
ai = list(map(int,input().split()))
bi = list(map(int,input().split()))
xi = [list(map(int, input().split())) for i in range(m)]
ans = []
ans.append(min(ai)+ min(bi))
for i in range(0,m):
    ans.append(ai[xi[i][0]-1] + bi[xi[i][1]-1] - xi[i][2])

print(min(ans))