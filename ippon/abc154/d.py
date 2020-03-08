#n = int(input())
n,k = map(int,input().split())
p_L = list(map(int,input().split()))

mydata = []

kazu = list(range(1,1001))
for i in p_L:

    kitai = sum(kazu[0:i])/i
    mydata.append(kitai)

res = [0] * (n+1)

res[0] = mydata[0]
for i in range(len(mydata)-1):
    res[i+1] = res[i] + mydata[i+1]

# print(mydata)
# print(res)
# print("----")
ans = 0
for i in range(n):
    tmp = res[i] - res[i-k]
    ans = max(ans,tmp)
    #print(mydata[i:i+k])
print(ans)

