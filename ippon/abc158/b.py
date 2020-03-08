n,a,b = map(int,input().split())
saaa = a+b
s1 = n//saaa
nokori = n%saaa
if nokori >= a:
    nokori = a
else:
    nokori = nokori
ans = s1*a + nokori
print(ans)