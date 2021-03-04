N = int(input())

K = (N-1) // 9 + 1
i = N - (K-1) * 9
print(str(str(i) * K))
