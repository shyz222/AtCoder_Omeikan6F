import sys
sys.setrecursionlimit(500000)

h,w = map(int,input().split())

c_L = []
reached = []

for i in range(h):
    tmp = list(input())
    c_L.append(tmp)

def dfs(x,y):
    global c_L
    global reached
    #print(reached)
    print(x,y)
    if x < 0 or y < 0:
        # print(reached)
        reached.append([x,y])
        return
    elif c_L[x][y]=="#":
        reached.append([x,y])
        return
    elif [x,y] in reached:
        return
    elif c_L[x][y] == "g":
        print("Yes")
        exit()
    else:
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)


dfs(0,0)
print("No")