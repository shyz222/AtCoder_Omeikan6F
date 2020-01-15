#n = int(input())
#a_L = map(int,input().split())
n,m = map(int,input().split())
dic = {}
for i in range(10**5+1):
    dic[str(i)] = "0"

ii = 0
check_dic = {}
counter = 0

for i in range(m):
    p,s = map(str,input().split())
    print(counter)
    if ii == 0:
        bango = p
        ii += 1

    if s == "WA":
        if dic[p] != "AC":
            counter += 1
    
    if bango != p:
        check_dic[p] = counter
        counter = 0

    if s == "AC":
        dic[p] = "AC"
print(check_dic)
