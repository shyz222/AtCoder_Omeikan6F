items = list(map(int, input().split()))
K = int(input())

print(sum(items)+max(items)*((2**K)-1))
