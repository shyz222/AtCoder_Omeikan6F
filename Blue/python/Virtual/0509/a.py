S, T = map(str, input().split())

if S.endswith('F') and T.endswith('F'):
    print(abs(int(S[0])-int(T[0])))
elif S.startswith('B') and T.startswith('B'):
    print(abs(int(S[1])-int(T[1])))
elif (S == '1F' and T == 'B1') or (S == 'B1' and T == '1F'):
    print('1')
elif S.startswith('B') and T.endswith('F'):
    print(int(S[1])+int(T[0])-1)
elif T.startswith('B') and S.endswith('F'):
    print(int(S[0])+int(T[1])-1)
