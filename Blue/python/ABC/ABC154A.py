S, T = map(str, input().split())
A, B = map(int, input().split())
U = str(input())

if U == S:
    A -= 1
else:B -= 1

print(A,B)