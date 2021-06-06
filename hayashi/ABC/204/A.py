x, y = list(map(int, input().split()))
hand = [0, 1, 2]
ans = 0
if x == y:
    ans = x

else:
    hand.remove(x)
    hand.remove(y)

    ans = hand[0]

print(ans)
