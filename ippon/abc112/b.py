n,t = map(int,input().split())

dic = {}
for val in range(n):
    c,ti = map(int,input().split())
    if ti <= t:
        dic[c] = ti

if dic == {}:
    print("TLE")
    exit()

# sort
dic = sorted(dic.items() ,key=lambda x:x[0])
print(dic[0][0])
