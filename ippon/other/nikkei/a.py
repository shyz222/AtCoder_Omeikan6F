#a,b = map(int,input().split())
n = int(input())
counter = 0
for a in range(1,n):
    b = n-a
    if b != a:
        #print("ab",a,b)
        counter += 1
print(counter//2)