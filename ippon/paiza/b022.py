m,n,k = map(int,input().split())
a_L = []

for val in range(k):
    a_L.append(int(input()))

# 広場分の人数追加
#a_L.append(0)

# dicの初期化
data_dic = {}
data_dic["0"]=n

# 演説者をとる
unique_L = set(map(str,a_L))


for val in unique_L:
    data_dic[val]=0

while a_L:
    counter = 0
    candidate = str(a_L.pop(0))

    # 支持なし層をもってくる処理
    if data_dic["0"] > 0:
        data_dic["0"] -= 1
        data_dic[candidate] += 1
    # 他の党から人をもってくる処理
    for val in unique_L:
        if candidate != val and data_dic[val] !=0:
            data_dic[val] -=1
            counter +=1

    data_dic[candidate] += counter

data_dic.pop("0")
#print(data_dic)

most_L = []
max_num = 0

for val in sorted(data_dic.items(),key=lambda x:x[1],reverse=True):
    max_num = max(val[1],max_num)
    if max_num == val[1]:
        most_L.append(val[0])


for val in sorted(most_L):
    print(val)
