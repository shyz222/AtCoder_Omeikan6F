N, M = list(map(int, input().split()))
# 隣接行列でとく必要なかった

# road_array = []
# for i in range(N):
#     road_array.append([0] * N)

# for i in range(M):
#     a, b = list(map(int, input().split()))
#     a -= 1
#     b -= 1

#     road_array[min(a, b)][max(a, b)] += 1
#     road_array[max(a, b)][min(a, b)] += 1

# for i in range(N):
#     print(sum(road_array[i]))

road_array = [0] * N

for i in range(M):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    road_array[a] += 1
    road_array[b] += 1

for i in road_array:
    print(i)
