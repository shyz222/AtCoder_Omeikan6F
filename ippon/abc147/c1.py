import sys

sys.setrecursionlimit(20000)


n = int(input())
#hatsugen_L = list(map(int,input().split()))

dic = {}
h_L = []
for val in range(n):
    a = int(input())
    
    for val in range(a):
        tmp = list(map(int,input().split()))
        h_L.append(tmp)
    #dic[val] = h_L

# for val in range(n):
#     a = int(input())
#     h_L = []
#     for val in range(a):
#         tmp = list(map(int,input().split()))
#         h_L.append(tmp)
#     dic[val] = h_L


ans = []

def dfs(hito,katei,result_L):

    global h_L
    global n
    print("----")
    print(hito)
    if hito == n-1:
        ans.append(sum(result_L))
        return
    
    if katei == 1:
        for val in h_L:
            #print(val)
            if val[0] == hito:
                if val[1] != 1:
                    return
    
    print(hito,result_L)
    result_L.append(katei)
    dfs(hito+1,0,result_L)
    dfs(hito+1,1,result_L)


dfs(0,0,[])
dfs(0,1,[])

print(ans)
print(max(ans))
print(h_L)
# def make_tf(hito,katei,result_L):
#     global n
#     global result
#     #print(n)
#     if hito == n-1:
#         #return result_L
#         result.append(result_L)
#     result_L.append(katei)
#     print(result_L)
#     make_tf(hito+1,0,result_L)
#     make_tf(hito+1,1,result_L)

# print(make_tf(0,0,result))

