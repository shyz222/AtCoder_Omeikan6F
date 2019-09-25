n = int(input())
a_L = list(map(int,input().split()))

a_L.append(-99)
tmp_num = -1
result_L = []
counter = 0

for val in range(len(a_L)):
    #print(tmp_num,a_L[val])

    if tmp_num == a_L[val]:
        counter += 1
    if tmp_num != a_L[val] and counter != 0:
        counter +=1
        result_L.append(counter)
        #print("a",tmp_num,a_L[val],counter)
        counter = 0

    tmp_num = a_L[val]


result_L = [i//2 for i in result_L]


print(sum(result_L))
