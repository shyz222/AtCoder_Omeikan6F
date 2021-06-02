A, B = list(map(int, input().split()))
nyu_kokei_bun = A + B

if nyu_kokei_bun >= 15 and B >= 8:
    print(1)
elif nyu_kokei_bun >= 10 and B >= 3:
    print(2)
elif nyu_kokei_bun >= 3:
    print(3)
else:
    print(4)
