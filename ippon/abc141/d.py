import heapq

n,m = map(int,input().split())
a_L = list(map(lambda x:int(x) * -1,input().split()))

heapq.heapify(a_L)
#a_L = list(sorted(a_L))
#max_num = a_L[0]
#a_L.append(max_num)

for val in range(0,m):
    a_min = heapq.heappop(a_L)
    a_min = (-1 * a_min)//2 * -1
    heapq.heappush(a_L,a_min)

print(-sum(a_L))

