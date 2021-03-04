# せいぜい555555通りなので全探索してもいける

N = int(input())

count = 0

for i in range(1, 555555 + 1):
    si = str(i)
    flag = True

# 対象（ゾロ目数）かどうかチェック
    for s in si:
        if s != si[0]:
            flag = False
# ゾロ目数なら数える
    if flag:
        count += 1
# 数えた結果該当の番号になればそれが答え
    if flag and count == N:
        ans = i

print(ans)
