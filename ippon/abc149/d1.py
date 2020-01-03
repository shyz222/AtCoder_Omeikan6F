n = int(input())

def is_prime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

while True:
    if is_prime(n):
        print(n)
        exit()
    n += 1


