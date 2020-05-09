import sys
N = int(sys.stdin.readline())

L0 = 2
L1 = 1
L = L1
Lmin = L0

if N == 1:
  print(1)
  sys.exit()
for i in range(2, N+1):

  Li = L + Lmin
  Lmin = L
  L = Li

print(Li)
