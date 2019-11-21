import sys
sys.setrecursionlimit(100000)

target_x,target_y = map(int,input().split())

if (target_x+target_y)%3 != 0:
    print(0)

COUNTER = 0
def dfs(x,y):
    if x == 0 and y == 0:
        global COUNTER
        COUNTER +=1
    elif x < 0 or y < 0:
        return 0

    x1 = x-1
    y1 = y-2
    #print(x1)
    dfs(x1,y1)

    x2 = x-2
    y2 = y-1
    dfs(x2,y2)

dfs(target_x,target_y)
mod = 10**9+7
print(COUNTER%mod)