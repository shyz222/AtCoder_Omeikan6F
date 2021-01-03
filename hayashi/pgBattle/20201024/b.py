import math 
from decimal import Decimal

N = Decimal(input())

ans = Decimal("1") / (Decimal("5") ** N)

print(ans)

ansStr = str(ans)
if "E" not in ansStr:
    print(ansStr)
else:
    splited = ansStr.split("E")
    numRight = "".join(splited[0].split(".")).rstrip("0")
    zeroCount = int(splited[1].lstrip("-")) - 1
    zeroString = "".zfill(zeroCount)
    numLeft = f"0.{zeroString}"
    print(numLeft + numRight) 