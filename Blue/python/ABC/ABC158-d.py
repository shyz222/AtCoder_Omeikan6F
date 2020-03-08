from collections import deque
S = deque(input())
Q = int(input())
querry = [list(map(str, input().split())) for i in range(Q)]
reverse = False
for i in range(Q):
    if querry[i][0] == '1':
        reverse = not reverse
    elif querry[i][0] == '2':
        if querry[i][1] == '1':
            if reverse:
                S.append(querry[i][2])
            else:
                S.appendleft(querry[i][2])
        elif querry[i][1] == '2':
            if reverse:
                S.appendleft(querry[i][2])
            else:
                S.append(querry[i][2])

ans=list(S)

if reverse:
    print("".join(reversed(ans)))
else:
    print("".join(ans))
