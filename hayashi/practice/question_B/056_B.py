W, a, b = map(int, input().split())
if(a > b):
  [a,b] = [b,a]

print(max(b-a-W,0))
