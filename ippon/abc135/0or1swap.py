import sys

n = int(input())
p = list(map(int,input().split()))


sorted_p = sorted(p)

limit = 2

index_L,value_L = [],[]
for val in range(0,n):
    if p[val] != sorted_p[val]:
        index_L.append(val)
        value_L.append(p[val])
        limit -= 1

        if limit <= 0:
            p[index_L[0]] = value_L[1]
            p[index_L[1]] = value_L[0]

            if p == sorted_p:
                print("YES")
            else:
                print("NO")
            
            sys.exit(0)

print("YES")

