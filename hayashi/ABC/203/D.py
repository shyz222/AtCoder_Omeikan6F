import statistics

N, K = list(map(int, input().split()))

park = []
for i in range(N):
    park_row = list(map(int, input().split()))
    park.append(park_row)

ans = 10 ** 9

if N - K == 0:
    ans_list = []
    for i in park:
        for j in i:
            ans_list.append(j)
    ans = statistics.median_low(ans_list)

else:
    for i in range(0, N-K + 1):
        for j in range(0, N-K+1):
            area = [l[i:K+i] for l in park[j:K+j]]
            flat_area = sum(area, [])
            temp = statistics.median_low(flat_area)
            if ans > temp:
                ans = temp


print(int(ans))
