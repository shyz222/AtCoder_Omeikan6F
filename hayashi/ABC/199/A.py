a, b, c = map(int, input().split())

ans = c**2 - a**2 - b**2

if ans > 0:
    print("Yes")
else:
    print("No")
