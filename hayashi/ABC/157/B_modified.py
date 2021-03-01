# from PAST本
bingo_card = []
for _ in range(3):
    row = list(map(int, input().split()))
    bingo_card.append(row)

# 穴を開ける用の二次元配列（[[false, false, false], [false, false, false], [false, false, false]]）を作る
# 穴が開いたらTrue
M = []
for i in range(3):
    # 1行分を表す一次元配列
    row = []
    for j in range(3):
        row.append(False)
    M.append(row)

N = int(input())

# 与えられる数字一つひとつを確認し、上で作った穴あけ用に穴を開ける
for _ in range(N):
    b = int(input())
    for i in range(0, 3):
        for j in range(0, 3):
            if A[i][j] == b:
                M[i][j] = True

bingo = False

for i in range(3):
    if M[i][0] and M[i][1] and M[i][2]:
        bingo = True

for i in range(3):
    if M[0][i] and M[1][i] and M[2][i]:
        bingo = True


if M[0][0] and M[1][1] and M[2][2]:
    bingo = True

if M[0][2] and M[1][1] and M[2][0]:
    bingo = True

if bingo:
    print("Yes")
else:
    print("No")
