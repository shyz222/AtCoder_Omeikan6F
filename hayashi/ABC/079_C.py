N = input()

def dfs(i,f):
    if i == 3:
         a = eval(f)
         if a == 7:
             print(f+"=7")
             exit()
    else:
        dfs(i+1, f+"+"+N[i+1])
        dfs(i+1, f+"-"+N[i+1])


dfs(0,N[0])
