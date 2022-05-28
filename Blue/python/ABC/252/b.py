n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

maxIndex = [i + 1 for i, x in enumerate(a) if x == max(a)]
ans = "No"
for i in maxIndex:
    for j in b:
        if i == j:
            ans = "Yes"

print(ans)