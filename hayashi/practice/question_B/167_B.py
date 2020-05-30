import sys
input = sys.stdin.readline

A, B, C, K = map(int, input().rstrip().split())

if A >= K :
  print(K)
elif A+B >= K:
  print(A)
else:
  print(A-(K-A-B))
