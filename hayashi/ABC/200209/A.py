Scolor, Tcolor = input().split()
S, T = map(int, input().split())
U = input()

if U == Scolor:
  print(S-1, T)
else:
  print(S, T-1)
