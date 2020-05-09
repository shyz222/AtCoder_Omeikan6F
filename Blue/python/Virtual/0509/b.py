S = str(input())
a = 0
b = 0
c = 0

for i in S:
    if i ==  'a':
        a += 1
    elif i == 'b':
        b += 1
    else:c += 1

if max(a,b,c) == a:
    print('a')
elif max(a,b,c) == b:
    print('b')
else:print('c')
