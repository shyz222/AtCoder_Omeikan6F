N = int(input())

length = len(str(N))

ans = 0
max_count_5_case = 1
max_count_4_case = (10**15-1) - (10**12 - 1)
max_count_3_case = (10**12-1) - (10**9 - 1)
max_count_2_case = (10**9-1) - (10**6 - 1)
max_count_1_case = (10**6-1) - (10**3 - 1)

if length == 16:
    ans = max_count_5_case*5 + max_count_4_case*4 + \
        max_count_3_case*3 + max_count_2_case * 2 + max_count_1_case

# max4回の範囲
elif 13 <= length <= 15:
    ans += max_count_3_case*3 + max_count_2_case * \
        2 + max_count_1_case + 4 * (N - (10**12 - 1))

# max3回
elif 10 <= length <= 12:
    ans += max_count_2_case * \
        2 + max_count_1_case + 3 * (N - (10**9 - 1))

elif 7 <= length <= 9:
    ans += max_count_1_case + 2 * (N - (10**6 - 1))

elif 4 <= length <= 6:
    ans += N - (10**3 - 1)

else:
    ans += 0

print(ans)
