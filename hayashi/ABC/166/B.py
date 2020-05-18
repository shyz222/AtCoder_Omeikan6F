N, K = map(int, input().split())
ans_list = []

for i in range(2*K):
  if(i%2==0):
    tmp = input()
    pass
  else:
    list_tmp = list(map(int, input().split()))
    for item in list_tmp:
      ans_list.append(item)

print(N - len(set(ans_list)))
