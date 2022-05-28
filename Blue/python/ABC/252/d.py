n = int(input())
a = list(map(int, input().split()))
m = 2 * 10 ** 5 + 10

cnt = [0] * m

for i in a:
    cnt[i] += 1

ans = n*(n-1)*(n-2)//6

for i in cnt:
    ans -= (i* (i-1)//2)*(n-i)
    ans -= (i*(i-1)*(i-2))//6

print(ans)