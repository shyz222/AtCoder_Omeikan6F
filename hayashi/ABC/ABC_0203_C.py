N, M = map(float, input().split())

xList = [int(i) for i in input().split()]
xList.sort()

distanse_list = []
if N > M:
    N = M

if N == M:
    print("0")
else:
    for i in range(len(xList)-1):
        distanse = xList[i+1] - xList[i]
        distanse_list.append(distanse)

    distanse_list.sort()
    print(sum(distanse_list[0:int(M - N)]))
