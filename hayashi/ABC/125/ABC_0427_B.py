N = int(input())
valueList = list(map(int, input().split()))
costList = list(map(int, input().split()))
S = 0
total = 0

for i in range(N):
    S = valueList[i] - costList[i]
    if S > 0:
        total += S
print(total)
