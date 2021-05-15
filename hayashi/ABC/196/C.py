import sys
N = int(input())

list_9 = [9,
          90,
          900,
          9000,
          90000,
          900000]

keta = len(str(N))

if N < 11:
    print(0)
elif keta == 2:
    if N < 22:
        print(1)
    elif N < 33:
        print(2)
    elif N < 44:
        print(3)
    elif N < 55:
        print(4)
    elif N < 66:
        print(5)
    elif N < 77:
        print(6)
    elif N < 88:
        print(7)
    elif N < 99:
        print(8)
    elif N == 99:
        print(9)

elif keta % 2 != 0:
    ans_keta = (keta-1)/2
    y = 0
    for i in range(int(ans_keta)):
        y += list_9[i]
    print(y)

else:
    # 前後半に分けた時の前半最後
    a = int((keta/2) - 1)
    top = 0
    if int(str(N)[0]) == 1:
        top = min(int(str(N)[a+1]), int(str(N)[0]))
    else:
        top = int(str(N)[0])
    if top == 0:
        ans_keta = (keta-2)/2
        s = 0
        for i in range(int(ans_keta)):
            s += list_9[i]
        print(s)
        sys.exit()
    max_par_keta = 10 ** (a)

    current = int(str(N)[-a:]) + 1

    y = 0

    for i in range(int(keta/2)-1):
        y += list_9[i]

    print(int((int(top)-1) * max_par_keta + current + y))
