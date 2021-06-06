N = int(input())

mountain = []
for i in range(N):
    S, T = map(str, input().split())
    T = int(T)

    mountain.append([S, T])

mountain = sorted(mountain, key=lambda height: height[1], reverse=True)

print(mountain[1][0])
