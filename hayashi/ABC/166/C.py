N, M = map(int, input().split())
keyList = list(range(1,N+1))
values = [True] * N
dic = dict(zip(keyList, values))
HList = list(map(int, input().split()))
ans = []

for i in range(M):
  a, b = map(int, input().split())
  H_a = HList[a-1]
  H_b = HList[b-1]
  if(H_a == H_b):
    dic[a] = False
    dic[b] = False
  elif(H_b > H_a):
    dic[a] = False
  elif(H_a > H_b):
    dic[b] = False


for i in range(1, len(dic.values())+1):
  if(dic[i] == True):
    ans.append(dic[i])
print(len(ans))
