A,B = map(int, input().split())

if A > B:
    if A-1 >B:
        print(A+(A-1))
    else:
        print(A+B)
elif A == B:
    print(A+B)
else:
    if B-1 >A:
        print(B+(B-1))
    else:
        print(A+B)
