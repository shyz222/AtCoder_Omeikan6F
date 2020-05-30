import sys
input = sys.stdin.readline

D, N = map(int, input().rstrip().split())


if N != 100:
  print(100 ** D * N)

else:
  print(100 ** D * (N+1))
