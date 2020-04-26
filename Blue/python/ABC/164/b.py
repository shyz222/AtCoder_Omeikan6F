A, B, C, D =  map(int, input().split())
T_count = 0 
A_count = 0
for i in range(100):
    C -= B
    T_count += 1
    if C <= 0:
        break

for j in range(100):
    A -= D
    A_count += 1
    if A <= 0:
        break

if T_count <= A_count:
    print('Yes')
else:print('No')