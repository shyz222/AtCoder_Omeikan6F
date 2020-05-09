N = int(input())
prices = []
for i in range(N):
  prices.append(int(input()))

prices_sum = sum(prices)
ans = prices_sum - (max(prices) / 2)

print(int(ans))
