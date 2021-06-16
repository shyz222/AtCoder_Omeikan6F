import bisect
import sys
sys.setrecursionlimit(10000000)


N, Q = list(map(int, input().split()))

A = list(map(int, input().split()))


def dfs(n, prev):
    ok = bisect.bisect_right(A, n)
    if ok == 0:
        print(n)
        return
    elif ok == prev:
        print(n)
        return
    diff = ok - prev
    dfs(n + diff, ok)


for i in range(Q):
    k = int(input())
    dfs(k, 0)
