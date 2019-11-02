s = input()
L = ["A","C","G","T"]

counter = 0
ans_L = []
for val in s:
    if val in L:
        counter += 1
    else:
        ans_L.append(counter)
        counter = 0
ans_L.append(counter)

print(max(ans_L))
