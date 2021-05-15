N = int(input())

stock_list = list(map(int, input().split()))

Q = int(input())

query_list = []

ans = 0

for i in range(Q):
    query_list.append(list(map(int, input().split())))

# セット販売を行ったカード1枚あたりの枚数
s = 0

# 全部売った枚数（1枚あたり）
z = 0


def single_sell(x, amount, ans, minStockAll, minStockSet, s, z):
    if x-1 % 2 == 0:
        card_x = stock_list[x-1] - s - z
    else:
        card_x = stock_list[x-1] - z

    if card_x < amount:
        return [ans, minStockAll, minStockSet]
    card_x -= amount
    ans += amount
    if x-1 % 2 == 0:
        minStockSet = min(stock_list[x-1], minStockSet)
    else:
        minStockAll = min(stock_list[x-1], minStockAll)
    return [ans, minStockAll, minStockSet]


def combo_sell(amount, minStockSet, s, z):
    if minStockSet - s - z >= amount:
        s += amount
    return [s]


def all_sell(amount, ans, minStockAll, minStockSet, s, z):
    for i in range(len(stock)):
        if stock[i] < amount:
            return [ans]
    for i in range(len(stock)):
        stock[i] -= amount
        ans += amount
    return [ans, minStockAll, minStockSet, z]


min_stock_set = 1000000000000
# sold_all = 1000000000000

min_stock_all = min(stock_list)

for i in range(len(stock_list)):
    min_if i % 2 == 0 and stock_set < stock_list[i]:
        min_stock_set = stock_list[i]


for query in query_list:
    if query[0] == 1:
        [ans, min_stock_all, min_stock_set] = single_sell(
            query[1], query[2], ans)
    elif query[0] == 2:
        [s] = combo_sell(
            query[1], min_stock_set, s, z)
    elif query[0] == 3:
        [ans,  min_stock_all, min_stock_set] = all_sell(query[1])

print(ans)
