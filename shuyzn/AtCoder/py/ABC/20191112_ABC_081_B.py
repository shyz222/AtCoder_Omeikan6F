# -*- coding:utf-8 -*-
n = int(input())
a = list(map(int, input().split()))

# 解1


def div_cnt(i):
    cnt = 0
    while i % 2 == 0:
        i /= 2
        cnt += 1
    return cnt


print(min(map(div_cnt, a)))


# 解2
# cnt = 0
# flag = True
# while flag:
#     for i in range(n):
#         if (a[i] % 2 == 0):
#             a[i] = a[i] // 2  # pythonは//で商、%で余り
#         else:
#             flag = False
#             break
#     cnt += 1
# print(cnt-1)
