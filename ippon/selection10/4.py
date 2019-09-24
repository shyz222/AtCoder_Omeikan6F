a = int(input())+1
b = int(input())+1
c = int(input())+1
x = int(input())

counter = 0

for _a in range(a):
    for _b in range(b):
        for _c in range(c):
            ans = 500*_a + 100*_b + 50*_c
            if ans == x:
                counter += 1

print(counter)
