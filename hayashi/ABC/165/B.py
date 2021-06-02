import math
X = int(input())

deposit = 100
ans = 0

while deposit < X:
    # 嘘解法→浮動小数点がらみの誤差で微妙に変わるらしい
    # deposit = math.floor(deposit * 1.01)
    deposit += deposit//100
    ans += 1

print(ans)
