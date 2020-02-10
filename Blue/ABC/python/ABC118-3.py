N = int(input())
mons =[int(i) for i in input().split()]


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

ans = mons[-1]
for i in mons:
    ans = gcd(ans, i)

print(ans)