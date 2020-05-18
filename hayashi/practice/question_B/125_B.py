import sys
input = sys.stdin.readline

N = int(input().rstrip())

V_list = list(map(int, input().rstrip().split()))
C_list = list(map(int, input().rstrip().split()))
ans_V = []
ans_C = []

for i in range(N):
  if V_list[i] > C_list[i]:
    ans_V.append(V_list[i])
    ans_C.append(C_list[i])

print(sum(ans_V) - sum(ans_C))
