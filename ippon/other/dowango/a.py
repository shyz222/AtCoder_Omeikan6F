n = int(input())
#a_L = map(int,input().split())
aaa,t_L = [],[]
for i in range(n):
    s,t = map(str,input().split())
    aaa.append(s)
    t_L.append(int(t))
x = input()

i = aaa.index(x)
print(sum(t_L[i+1:]))

