n = int(input())
#hatsugen_L = list(map(int,input().split()))
h_L = []

dic = {}

for val in range(n):
    a = int(input())
    h_L = []
    for val in range(a):
        tmp = list(map(int,input().split()))
        h_L.append(tmp)
    dic[val] = h_L

man_L = []


def dfs(hito,katei,result):
    # katei = 0が or 1

    if hito == n-1:
        return result

    if katei == 1:
        for val in dic[hito]:
            if val[0] == hito and katei ==1:
                if val[1] != katei:
                    print(val[1],katei)
                    #print("aaa")
                    return
        
    result.append(katei)

    dfs(hito+1,0,result)
    dfs(hito+1,1,result)


ans1 = dfs(0,0,result1)
ans2 = dfs(0,1,result2)

print(ans1,ans2)
