n, a, b = map(int, input().split())
law = 10 ** 9 + 7

def fermat(n, r, law):
    x = 1
    y = 1
    for i in range(r):
        x = x * (n - i) % law
        y = y * (i + 1) % law

    ans = x * pow(y, law - 2, law) % law
    return ans

print((pow(2, n, law) - 1 - fermat(n, a, law) - fermat(n, b, law)) % law)
