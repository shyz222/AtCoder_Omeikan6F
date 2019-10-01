def dfs(i,s):
    if i==0:
        print(s)
    else:
        for val in ["a","b","c"]:
            dfs(i-1,s+val)

if __name__=="__main__":
    n = int(input())
    dfs(n,"")
