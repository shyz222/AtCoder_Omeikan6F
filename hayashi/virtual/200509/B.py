import sys

S = sys.stdin.readline()
Alen = 0
Blen = 0
Clen = 0
for i in range(len(S)):
  if(S[i]=='a'):
    Alen += 1
  if(S[i]=='b'):
    Blen += 1
  if(S[i]=='c'):
    Clen += 1
highest = max(Alen, Blen, Clen)

if(highest == Alen):
  print('a')
elif highest == Blen:
  print('b')
else:
  print('c')
