n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
b.append(0)
result_L = []
yoryoku_L = [0]

for val in range(n+1):
    yoryoku = yoryoku_L[val] + b[val] - a[val]

    if yoryoku >= 0:
        result = a[val]

        if a[val] - yoryoku_L[val] >= 0:
            yoryoku_L.append(yoryoku)
        else:
            yoryoku_L.append(b[val])

        result_L.append(result)
    else:
        result = b[val] + yoryoku_L[val]
        yoryoku_L.append(0)
        result_L.append(result)


print(sum(result_L))
