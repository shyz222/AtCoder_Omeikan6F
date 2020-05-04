S = int(input())
ans_list = []
i = 0
while S not in ans_list:
  ans_list.append(S)
  if(S % 2 == 0):
    S = S/2
  else:
    S = 3 * S + 1
  i += 1

print(i+1)
