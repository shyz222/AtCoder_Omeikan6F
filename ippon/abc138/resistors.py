n = int(input())
a_L = list(map(int,input().split()))

result = 0.0
for val in a_L:
    result = result + 1/float(val)
result = 1/result

print(result)
