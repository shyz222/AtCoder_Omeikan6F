import math
def makeInt(n):
    return int(n)

N = int(input())
line = list(map(makeInt,list(input().split())))

newList = []
for i in range(len(line) - 1):
    newList.append(line[i+1]-line[i])

sums = 0
for j in range(len(newList) - 2):
    sums= sum(newList[j:N-1])
    sums += sum
ans = sum(newList)*len(newList)+sums+newList[len(newList)]

fact = math.factorial(N - 2)
answer = ans*fact

if(answer < 10**9):
    print(answer)
else:
    print(answer % (10**9+7))
