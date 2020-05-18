import sys
input = sys.stdin.readline

N = (input().rstrip())
if N[-1] == "3":
  print('bon')
elif N[-1] == '0' or N[-1] == '1' or N[-1] == '6' or N[-1] == '8':
  print('pon')
else:
  print('hon')
