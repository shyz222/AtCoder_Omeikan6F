#n = int(input())
s,t = map(str,input().split())
a,b = map(int,input().split())
u = input()

#a_L = list(map(int,input().split()))

if u == s:
    print(a-1,b)
else:
    print(a,b-1)