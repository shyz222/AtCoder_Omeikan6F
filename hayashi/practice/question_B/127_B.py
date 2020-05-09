r, D, X0 = map(int, input().split())
for i in range(10):
  X0 = r*X0 - D
  print(X0)
