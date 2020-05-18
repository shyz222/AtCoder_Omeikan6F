import sys
input = sys.stdin.readline

K = int(input().rstrip())
S = input().rstrip()

if len(S) <= K:
  print(S)
else:
  print(S[:K] + '...')
