N, K  = map(int, input().split())
for i in range(N):
  ans = K * (K-1)**(N-1)

print(ans)
