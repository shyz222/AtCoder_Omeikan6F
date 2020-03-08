S = input()
a = [str(c) for c in S]

for i in range(len(a)):
    a[i] = "x"

ans = ''.join(a)
print(a)