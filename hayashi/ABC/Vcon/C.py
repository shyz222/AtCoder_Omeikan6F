N = int(input())
list = list(map(int, input().split()))

list_ans = []
for i in range(N):
    list_ans.append(abs(sum(list[0:i]) - sum(list[i:N])))

print(min(list_ans))
