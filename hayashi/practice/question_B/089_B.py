import sys
input = sys.stdin.readline

N = int(input().rstrip())
array = input().rstrip().split()

if 'Y' not in array:
  print('Three')
else:
  print('Four')
