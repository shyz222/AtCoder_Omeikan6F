l = list(map(int, input().split()))
b = l[1]
sort_l = sorted(l)

if b==sort_l[1]:
    print("Yes")
else: print("No")