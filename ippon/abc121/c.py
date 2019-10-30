n,m = map(int,input().split())

dic,new_dic = {},{}
for val in range(n):
    a,b = map(int,input().split())
    dic[a] = b

dic = sorted(dic.items(),key=lambda x:x[0])

for val in dic:
    new_dic[val[0]] = val[1]

ans = 0

#print(new_dic)

for k,v in new_dic.items():
    if m - v > 0:
        ans += k*v
        m = m-v

    elif m - v <= 0:
        ans += k*m
        print(ans)
        exit()
