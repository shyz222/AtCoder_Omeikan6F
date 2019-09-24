n = int(input())

a_L = []
for val in range(n):
    a_L.append(int(input()))

a_L = list(set(a_L))
print(len(a_L))
