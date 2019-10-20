import copy

n,l = map(int,input().split())

n_L = list(range(n))
a_L = list(map(lambda x:l+x,n_L))
# out of rangeを防ぐため
a_L.append(0)

allsum = sum(a_L)

result_L = []

diff = abs(allsum-sum(a_L[1:]))

for val in range(n):
    b_L = copy.copy(a_L)
    b_L.pop(val)
    temp_sum = sum(b_L)

    if abs(allsum-temp_sum) <= diff:
        result = temp_sum
    diff = abs(allsum-temp_sum)

print(result)


