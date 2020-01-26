import fractions
x,y = map(int,input().split())
ans = (x*y)/(fractions.gcd(x, y))
print(round(ans))