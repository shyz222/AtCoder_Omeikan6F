N, X = map(int, input().split())
suu = [int(i) for i in input().split()]
flop,flag =0,1 

for i in range(N):
    flop += suu[i]
    if flop <= X:
        flag += 1

print(flag)