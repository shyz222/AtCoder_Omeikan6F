N, A, B = map(int, input().split())
ans = N//(A+B) * A
tmp = N%(A+B)

print(ans + min(tmp, A))
