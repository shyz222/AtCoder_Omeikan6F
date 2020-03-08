S = str(input())
ans_h = 0
ans_i = 0
count_h = 0
count_i = 0

for i in range(0,len(S),2):
    if S[i] != 'h':
        ans_h += 1
    else:
        count_h += 1

for j in range(1,len(S),2):
    if S[j] != 'i':
        ans_i += 1
    else:
        count_i += 1

if ans_h == 0 and ans_i == 0 and count_h == count_i:
    print('Yes')
else:print('No')