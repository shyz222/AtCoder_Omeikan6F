a = list(input().split(" "))
h = list(input().split(" "))

lider = []
for h_s in h:
    if int(h_s) >= int(a[1]):
        lider.append(h_s)

print(len(lider))
