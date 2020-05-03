N, L = map(int,input().split())
list_S = []
for i in range(N):
  S = input()
  list_S.append(S)

sorted_list_S = sorted(list_S)
ans = ''.join(sorted_list_S)

print(ans)
