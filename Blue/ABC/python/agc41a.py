N, A, B= map(int,input().split())

if (A+B)%2 == 0:
    print(round((A+B)/2-A))
elif (A+B)%2 != 0:
    if A == 2:
        print(N-B)
    elif A== 1:
        print(B-1)
    elif B == N-1:
        print(N-A)
    elif B == N:
        print(B-A)