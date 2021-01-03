H, W = map(int, input().split())

mapping_array = []
for height in range(H):
    items = list(map(int, input().split()))
    mapping_array.append(items)

mapping_array_flatten = sum(mapping_array, [])
min_item = min(mapping_array_flatten)

ans = 0

for item in mapping_array_flatten:
    diff = item - min_item
    ans += diff

print(ans)
