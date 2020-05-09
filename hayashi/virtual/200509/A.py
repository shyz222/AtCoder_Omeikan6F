import sys
floor = [ 'B9','B8','B7','B6','B5','B4','B3','B2','B1','1F','2F','3F','4F','5F','6F','7F','8F','9F' ]

S,T = sys.stdin.readline().split()
Shight = 0
Thight = 0
for i in range(len(floor)):
  if(floor[i] == S):
    Shight = i
  if(floor[i] == T):
    Thight = i

print(abs(Shight-Thight))
