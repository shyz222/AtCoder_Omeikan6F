import sys
input = sys.stdin.readline

N = int(input().rstrip())
S = input().rstrip()

if N % 2 != 0:
  print('No')
  sys.exit()
if S[:int(N/2)] == S[int(N/2):]:
  print('Yes')
else:
  print('No')
