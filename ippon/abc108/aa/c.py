n = int(input())
L = []
for i in range(n):
    L.append(int(input()))

L_sorted = sorted(L,reverse=True)
for i in L:
    if i == L_sorted[0]:
        print(L_sorted[1])
    else:
        print(L_sorted[0])

# こいつはn **16 = 10**8**16
#3
#[1,4,3]
#[4,3,1]


