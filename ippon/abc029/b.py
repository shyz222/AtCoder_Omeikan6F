
counter = 0
for val in range(12):
    L = []
    n = input()
    L = [val for val in n]
    if "r" in L:
        counter += 1
        continue
print(counter)
