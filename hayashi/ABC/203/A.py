a, b, c = list(map(int, input().split()))

if a == b:
    print(c)
elif a == c:
    print(b)
elif b == c:
    print(a)
else:
    print(0)
