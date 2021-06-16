H, W = list(map(int, input().split()))

array = []
for h in range(H):
    temp = list(map(int, input().split()))
    array.append(temp)
ans = []
for index, item in enumerate(array):
    sum_item = sum(item)
    temp = [sum_item] * W
    for w in range(W):
        temp_sum_w = []
        # for h in range(H):
        temp_sum_w.append(array[index][w])
        x = sum(temp_sum_w) - array[index][w]
        temp[w] += x
    ans.append(temp)

for item in ans:
    print(*item)
