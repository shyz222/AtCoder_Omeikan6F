N = int(input())

playList = []
timeList = []
for cnt in range(N):
    ttl, scd=input().split()
    playList.append(ttl)
    timeList.append(int(scd))

key = input()
index = int(playList.index(key))

print(sum(timeList[index+1: N]))
