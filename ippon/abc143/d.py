from itertools import combinations
n = int(input())
#a,b = map(int,input().split())
a_L = list(map(int,input().split()))
counter = 0
for i in combinations(a_L,3):
    if abs(i[0]-i[1]) < i[2] and i[2] < i[0] + i[1]:
        counter += 1
    elif abs(i[1]-i[2]) < i[0] and i[0] < i[1] + i[2]:
        counter += 1
    elif abs(i[2]-i[0]) < i[1] and i[1] < i[2] + i[0]:
        counter += 1
print(counter)
