import sys
input = sys.stdin.readline

S = input().rstrip()
S32 = S[2:-1]
trimed_S = S32.replace('C', '', 1)
ac_cut_S = S.replace('A', '', 1).replace('C', '', 1)

ans = 'AC'
if S[0] != 'A':
  ans = 'WA'
elif (not ac_cut_S.islower()) or len(S32) - len(trimed_S) != 1:
  ans = 'WA'

print(ans)
