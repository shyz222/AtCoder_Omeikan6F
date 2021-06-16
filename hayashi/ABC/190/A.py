a, b, c = list(map(int, input().split()))

if a > b:
    print("Takahashi")
elif b > a:
    print("Aoki")
elif c == 1:
    print("Takahashi")
else:
    print("Aoki")
