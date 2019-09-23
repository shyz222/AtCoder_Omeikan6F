n = int(input())
b = list(map(int,input().split()))

b.append(b[-1])

s = b[0]

for val in range(0,n-1):
    s = s + min(b[val],b[val+1])

print(s)
