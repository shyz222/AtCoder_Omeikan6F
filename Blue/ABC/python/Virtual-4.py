N = int(input())
A = list(map(int, input().split()))
ans = 0
while all(i % 2 == 0 for i in A):
    A = [i / 2 for i in A]
    ans += 1
print(ans)