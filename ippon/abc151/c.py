#n = int(input())
#a_L = map(int,input().split())
n,m = map(int,input().split())
dic = {}
for i in range(10**5+1):
    dic[str(i)] = "0"
ac_dic = {}
wa_c = 0

for i in range(m):
    p,s = map(str,input().split())
    if s =="AC":
        dic[p] = "AC"
        ac_dic[p] = "AC"

    if s == "WA" and dic[p] != "AC":
        wa_c += 1


#print(ac_dic)
print(len(ac_dic),wa_c)
