n = int(input())

p_L = list(map(int,input().split()))


counter = 0
for val in range(n-2):
    _tmp = p_L[val:val+3]
    a = _tmp[1]
    b = sorted(_tmp)[1]
    if a==b:
        counter += 1
print(counter)
