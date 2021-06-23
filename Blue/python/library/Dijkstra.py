from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float("INF")

#solve
def solve():
    n, m = LI()
    ab = LIR_(m)
    def Dijkstra(num, start, vedge):
        """ vedge は DAG の 重みとして vedge[from] = (to, value)　としておくこと """
        """ DAGでない場合は vedge[from] と vedge[to] の両方を作ること """
        """ dist[i] は start から i までの最短距離 """
 
        dist = [float("inf") for i in range(num)]
        dist[start] = 0
        q = [[dist[start], start]]
        while q:
            du, u = heappop(q)
            for j, k in vedge[u]:
                if dist[j] > du + k:
                    dist[j] = du + k
                    heappush(q, [dist[j], j])
        return dist
    edg = defaultdict(list)
    for a, b in ab:
        edg[a].append((b,1))
        edg[b].append((a,1))
    dist = Dijkstra(n, 0, edg)
    if inf in dist:
        print("No")
        return
    print("Yes")
    ans = [None] * n
    q = deque()
    q.append(0)
    while q:
        p = q.popleft()
        for e, _ in edg[p]:
            if ans[e] == None:
                if dist[p] + 1 == dist[e]:
                    ans[e] = p
                    q.append(e)
    for i in ans[1:]:
        print(i+1)
    return

#main
if __name__ == '__main__':
    solve()