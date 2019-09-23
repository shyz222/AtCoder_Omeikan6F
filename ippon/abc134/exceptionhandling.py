n = int(input())

a_L = []
for val in range(n):
    a_L.append(int(input()))

s_L = sorted(a_L)

for val in a_L:
    if s_L[-1] != val:
        print(s_L[-1])
    else:
        print(s_L[-2])
