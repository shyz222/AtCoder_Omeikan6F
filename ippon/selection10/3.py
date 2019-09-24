import sys

n = int(input())
a_L = list(map(int,input().split()))
counter = 0


while True:
    for val in a_L:
        if val % 2 != 0:
            print(counter)
            sys.exit(0)
    counter +=1
    a_L = [i/2 for i in a_L]
