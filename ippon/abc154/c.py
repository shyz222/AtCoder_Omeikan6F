n = int(input())
#a,b = map(int,input().split())
a_L = list(map(int,input().split()))
#print(a_L)
if len(a_L) == len(set(a_L)):
    print("YES")
else:
    print("NO")
