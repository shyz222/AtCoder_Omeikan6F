n = int(input()) + 1
ans = 0


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

for val in range(n):
    if len(make_divisors(val)) == 8 and val%2 != 0:
        ans += 1
print(ans)
