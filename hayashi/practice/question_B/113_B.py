N = int(input())
T, A = map(int, input().split())

H_list = list(map(int, input().split()))
ans_list = []

for i in H_list:
  kion = T - (i * 0.006)
  kion_abs = abs(kion - A)
  ans_list.append(kion_abs)

print(ans_list.index(min(ans_list))+1)
