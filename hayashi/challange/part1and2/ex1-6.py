n = int(input())
array = list(map(int, input().split()))

# print(n, array)

array.sort(reverse=True)
if len(array) >= 3:
    i = 0
    while True:
        sum = array[i + 1] + array[i + 2]
        if sum > array[i]:
            answer = sum + array[i]
            print(answer)
            break
        i += 1
else:
    print(0)
