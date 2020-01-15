import copy

n,m = map(int,input().split())
dic = {}

for i in range(m):
    p,y = map(int,input().split())
    dic[y] = p

sd = copy.deepcopy(dic)
#print(sd.items())
sd = sorted(sd.items(),key=lambda x:x[0])
sd = sorted(sd,key=lambda x:x[1])

ken = sd[0][1]
counter = 0
ans_dic = {}

for y,k in sd:
    if ken == k:
        counter +=1
    else:
        counter = 1
        ken = k
    tmp = str(k).zfill(6) + str(counter).zfill(6)
    ans_dic[y] = tmp

for i in dic.keys():
    print(ans_dic[i])
