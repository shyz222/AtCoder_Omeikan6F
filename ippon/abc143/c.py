n = input()
a_L = input()
a_L = [val for val in a_L ]

from itertools import groupby
counter = 0

for key, value in groupby(a_L):
    counter += 1

print(counter)
