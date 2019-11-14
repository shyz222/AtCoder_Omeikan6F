n = int(input())
a_L = []
for val in range(n):
    a_L.append(int(input()))

a_L = sorted(a_L,reverse=True)
a_L[0] /=2
print(int(sum(a_L)))