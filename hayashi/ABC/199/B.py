N = int(input())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

max_A = max(A_list)
min_B = min(B_list)

if max_A > min_B:
    print(0)
else:
    print(min_B - max_A + 1)
