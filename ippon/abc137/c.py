import copy
n = int(input())
r_L = list(map(int,input().split()))
l_L = copy.deepcopy(r_L)
l_L.reverse()


r_ans,l_ans = 0,0
r_ans_L,l_ans_L = [],[]

for val in range(n-1):
    if r_L[val] >= r_L[val+1]:
        r_ans += 1
    else:
        r_ans_L.append(r_ans)
        r_ans = 0
    



l_ans_L.append(l_ans)
r_ans_L.append(r_ans)

print(max(max(l_ans_L),max(r_ans_L)))
