N = int(input())
list = list(map(int, input().split()))

point = round(sum(list)/N)

ans_list = []
for item in list:
  ans_list.append((point - item)**2)

print(sum(ans_list))
