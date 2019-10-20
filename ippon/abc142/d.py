import itertools
import math 

a,b = map(int,input().split())

def divisor(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

if is_prime(a) and is_prime(b):
    print(1)
    import sys
    sys.exit()

a_L = divisor(a)
b_L = divisor(b)

kouyaku = set(a_L) & set(b_L)

new_L = []

for val in kouyaku:
    if is_prime(val):
        new_L.append(val)

new_L.append(1)
print(len(new_L))
#counter =0

#v = itertools.combinations(list(new_L),2)


#for i in v:

#    if math.gcd(i[0], i[1]) == 1:
        #print(i[0],i[1])
#        counter +=1
#print(counter)

