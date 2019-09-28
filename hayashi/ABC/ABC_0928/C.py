n = int(input())
a = list(map(int, input().split(" ")))
list = [a.index(x)+1 for x in range(1, n+1)]
print(*list)

# i = 1
# for a_s in a:
#     print(a.index(i)+1)
#     i += 1
