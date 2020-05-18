dict = {}
N, M = input().split(" ")

ACList = []
WAdict = {}
statusDict = {}
i = 1
while i <= int(M):
    key, ans = input().split(" ")
    if (ans == "AC"):
        ACList.append(key)
        statusDict[str(key)] = "OK"
    elif (ans == "WA" and key not in WAdict and key not in statusDict):
        WAdict[key] = 1
    elif (ans == "WA" and key in WAdict and key not in statusDict):
        WAdict[key] += 1

    i += 1

ACList = set(ACList)

penaList = []
for ACListItem in ACList:
    if (ACListItem in WAdict):
        penaList.append(WAdict[ACListItem])
print(len(set(ACList)), sum(penaList))
