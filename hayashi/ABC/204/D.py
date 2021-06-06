N = int(input())
T = list(map(int, input().split()))


list_a = []
list_b = []

T = sorted(T, reverse=True)

for i in range(len(T)):
    sum_a = sum(list_a)
    sum_b = sum(list_b)
    if sum_a > sum_b:
        list_b.append(T[i])
    else:
        list_a.append(T[i])

print(max(sum(list_a), sum(list_b)))
