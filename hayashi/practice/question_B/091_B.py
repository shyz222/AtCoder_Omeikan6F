import sys
input = sys.stdin.readline

Sdict = {}
Tdict = {}
N = int(input().rstrip())
for i in range(N):
  item = input().rstrip()
  if item not in Sdict.keys():
    Sdict[item] = 1
  else:
    Sdict[item] += 1
M = int(input().rstrip())
for i in range(M):
  item = input().rstrip()
  if item not in Tdict.keys():
    Tdict[item] = 1
  else:
    Tdict[item] += 1

ans_dict = {'0': 0}
for i in Sdict.keys():
  S = Sdict[i]
  if i not in Tdict:
    T = 0
  else:
    T = Tdict[i]
  ans_dict[i] = S-T

print(max(ans_dict.values()))
