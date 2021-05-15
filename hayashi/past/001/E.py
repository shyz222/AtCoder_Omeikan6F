N, Q = list(map(int, input().split()))
log_list = []
for i in range(Q):
    S = input().split()
    log_list.append(S)

# N*Nの隣接行列（問題の都合上falseじゃなくて N ）を作る

follow_list = []
for i in range(N):
    row = []
    for j in range(N):
        row.append("N")
    follow_list.append(row)


def single_follow(followList, a, b):
    followList[a-1][b-1] = "Y"
    return followList


def follow_back(followList, a):
    for i in range(N):
        if followList[i][a-1] == "Y":
            followList[a-1][i] = "Y"
    return followList


def follow_follow(followList, a):
    follow_pend_list = []
    for i in range(N):
        if followList[a-1][i] == "Y":
            for j in range(N):
                if followList[i][j] == "Y":
                    # followList[a-1][j] = "Y"
                    follow_pend_list.append([a-1, j])

    for item in follow_pend_list:
        if item[0] != item[1]:
            followList[item[0]][item[1]] = "Y"
    return followList


for list_item in log_list:
    if list_item[0] == "1":
        follow_list = single_follow(
            follow_list, int(list_item[1]), int(list_item[2]))
    elif list_item[0] == "2":
        follow_list = follow_back(follow_list, int(list_item[1]))
    elif list_item[0] == "3":
        follow_list = follow_follow(follow_list, int(list_item[1]))

for item in follow_list:
    print("".join(item))
    # print(*item)
