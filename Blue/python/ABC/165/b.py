import math

X = int(input())
yokin = 100
ans = 0
while yokin < X:
    yokin = int(yokin*1.01)
    
    ans += 1

print(ans)