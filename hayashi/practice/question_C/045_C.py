list = list(input())

a, b, c, d = map(int, list)


def plus(items, key):
    if(key == 1):
        return items[0] + items[1]
    else:
        return items[0] - items[1]


def numToOp(num):
    return "+" if num == 1 else "-"


ans = 0
opList = [1, 1, 1]
i = 0
while ans != 7:
    aPlusB = plus([a, b], opList[0])
    aPlusBPlusC = plus([aPlusB, c], opList[1])
    ans = plus([aPlusBPlusC, d], opList[2])
    # print(f"{i}回目：ans == {ans}, opList == {opList}")

    if ans != 7 and i <= 4:
        opList[i % 3] *= -1
        i += 1
    elif ans != 7 and i == 5:
        opList = [1, -1, 1]
        i += 1
    elif ans != 7 and i == 6:
        opList = [-1, 1, -1]
        i += 1

# print(opList)

print(
    f"{a}{numToOp(opList[0])}{b}{numToOp(opList[1])}{c}{numToOp(opList[2])}{d}=7")
