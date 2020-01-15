#n = int(input())
#a_L = map(int,input().split())
n,m = map(int,input().split())
dic = {}
for i in range(10**5+1):
    dic[str(i)] = "0"
ac_dic = {}
wa_c = 0
check_dic = {}

ii = 0
for i in range(m):
    p,s = map(str,input().split())
    if ii == 0:
        bango = p
        ii += 1

    if bango != p:
        wa_c = 0
    # pena
    if s == "WA":
        if bango == p and dic[p] != "AC":
            wa_c += 1

    check_dic[p] = wa_c
    # 解けた問題
    if s =="AC":
        ac_dic[p] = "AC"
        dic[p] = "AC"
    bango = p


print(check_dic)
counter = 0
for k,v in check_dic.items():
    if dic[k] == "AC":
        counter += v

#print(ac_dic)
print(len(ac_dic),counter)
