A, B, C = list(map(int, input().split()))

if C % 2 == 0:
    A = abs(A)
    B = abs(B)

if A > B:
    print(">")
elif B > A:
    print("<")
else:
    print("=")
