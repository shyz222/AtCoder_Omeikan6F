N = int(input())
A = list(input().split())

def has_duplicates(seq):
    return len(seq) != len(set(seq))

if has_duplicates(A):
    print('NO')
else:print('YES')