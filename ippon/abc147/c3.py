import itertools

n = int(input())

dic = {}


for val in range(n):
    a = int(input())
    h_L = []
    for _ in range(a):
        a1,a2 = list(map(int,input().split()))
        tmp = [a1-1,a2]
        h_L.append(tmp)
    dic[val] = h_L

ans = []

bit = itertools.product([0,1],repeat=n)
#bit = [(1,1,0)]
for val in bit:
    flag = True
    for i,katei in enumerate(val):
        if katei == 0:
            continue
        if katei == 1:
            for hatsugen in dic[i]:
                if hatsugen[1] != val[hatsugen[0]]:
                    flag = False

    if flag is True:
        ans.append(sum(val))

print(max(ans))
