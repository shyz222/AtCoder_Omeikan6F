import itertools

a_L = []

for i in range(5):
    a_L.append(int(input()))

def hosei(x):
    """int:x"""
    x = -(x // -10)
    return x*10

a_L = list(itertools.permutations(a_L))

ans_L = []

for c in a_L:
    times = 0
    counter = 0
    for i in c:
        if counter != 4:
            times += hosei(i)
        else:
            #print(aaa)
            times += i
        counter += 1
    ans_L.append(times)

print(min(ans_L))
