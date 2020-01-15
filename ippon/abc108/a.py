n = int(input())
if n%2==0:
  k,g = n/2,n/2
else:
  k,g = n//2,n//2+1
print(int(k*g))
