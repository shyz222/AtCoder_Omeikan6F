N = int(input())
house = list(map(int, input().split()))

house = set(house)

print(max(house) - min(house))
