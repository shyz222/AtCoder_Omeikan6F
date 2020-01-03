x = int(input())

if x==2:
    print(x)
    exit()

if x%2 == 0:
    x += 1

def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

while True:
    if is_prime(x):
        print(x)
        exit()
    x+=1
