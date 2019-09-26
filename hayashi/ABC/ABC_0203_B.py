N = input()

sides = [int(i) for i in input().split()]
lMax = max(sides)
lSum = sum(sides) -lMax
if lSum > lMax:
    print("Yes")
else:
    print("No")
