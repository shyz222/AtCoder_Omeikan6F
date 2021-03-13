A, B, W = list(map(int, input().split()))

min_count = 0
max_count = 0


W_gram = 1000 * W
diff_mikan = B - A

flag = False

# みかんの数（かも？
max_mikan_amount = W_gram // A
max_mikan_amari = W_gram % A

if max_mikan_amari <= diff_mikan * max_mikan_amount:
    ans_max = max_mikan_amount
else:
    flag = True

min_mikan_amount = W_gram // B
min_mikan_amari = W_gram % B

if min_mikan_amari == 0:
    ans_min = min_mikan_amount
elif A - min_mikan_amari <= diff_mikan * min_mikan_amount:
    ans_min = min_mikan_amount + 1
else:
    flag = True

if flag == True:
    print("UNSATISFIABLE")
else:
    print(*[ans_min, ans_max])
