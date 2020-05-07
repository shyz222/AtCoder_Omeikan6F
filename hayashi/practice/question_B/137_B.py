K, X = map(int, input().split())

ans_range = list(range(X-K+1,X+K))
ans_range = ' '.join(map(str, ans_range))
print(ans_range)
