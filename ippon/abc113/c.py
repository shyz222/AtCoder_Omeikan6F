import copy
n,m = map(int,input().split())

dic = {}
for i in range(m):
    c,y = map(int,input().split())
    dic[y] = c
#print(dic)

dic2 = copy.deepcopy(dic)
#print(dic)
dic2 = sorted(dic2.items(),key=lambda x:x[1],reverse=True)
dic2 = sorted(dic2.items(),key=lambda x:x[0])#,reverse=True)
#print(dic2)
#[(32, 1), (12, 1), (63, 2)]

ken = dic2[0][1]
counter = 0
ans = {}

for y,k in dic2:
    if ken == k:
        counter +=1
    else:
        counter = 1
    tmp = str(k).zfill(6) + str(counter).zfill(6)
    ans[y] = tmp

for i in dic.keys():
    print(ans[i])
