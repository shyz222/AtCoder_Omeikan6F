import math
n, a, b =map(int, input().split())
lcm = a * b // math.gcd(a, b)
n_a = n//a
n_b = n//b
n_l = n//lcm
sum_a = n_a*(2*a+(n_a-1)*a)//2
sum_b = n_b*(2*b+(n_b-1)*b)//2
sum_l = n_l*(2*lcm+(n_l-1)*lcm)//2
sum=n*(2*1+(n-1)*1)//2
print(int(sum-sum_a-sum_b+sum_l))
