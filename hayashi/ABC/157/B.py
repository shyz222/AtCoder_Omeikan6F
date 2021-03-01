def bingo_row(card, items):
    flag = False
    for row in card:
        if (row[0] in items and row[1] in items and row[2] in items):
            flag = True

    return flag


def bingo_col(card, items):
    flag = False
    for i in range(len(card)):
        if (card[0][i] in items and card[1][i] in items and card[2][i] in items):
            flag = True

    return flag


def bingo_cross(card, items):
    flag = False
    if ((card[0][0] in items and card[1][1] in items and card[2][2] in items)
            or (card[0][2] in items and card[1][1] in items and card[2][0])):
        flag = True

    return flag


row_1 = list(map(int, input().split()))
row_2 = list(map(int, input().split()))
row_3 = list(map(int, input().split()))
bingo_card = [row_1, row_2, row_3]

N = int(input())

items = []
for i in range(N):
    b = int(input())
    items.append(b)

if bingo_row(bingo_card, items) or bingo_col(bingo_card, items) or bingo_cross(bingo_card, items):
    print("Yes")
else:
    print("No")
