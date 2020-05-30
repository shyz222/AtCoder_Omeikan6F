N = int(input())
H_list = list(map(int, input().split()))



for i in range(len(H_list)):
    if i ==0:
        H_max = H_list[0]
        count = 1

    elif H_max <= H_list[i]:

        count += 1
        H_max = H_list[i]

print(count)
