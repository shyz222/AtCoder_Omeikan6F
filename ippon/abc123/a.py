diff_L = []
for val in range(5):
    a = int(input())
    diff_L.append(a)

k = int(input())
ans = max(diff_L)-min(diff_L)

if ans <= k:
    print("Yay!")
else:
    print(":(")
