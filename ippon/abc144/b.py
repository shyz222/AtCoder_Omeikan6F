n = int(input())
#a_L = list(map(int,input().split()))

for val in range(1,n+1):
    if n % val == 0 and val < 10 and n/val < 10:
        print("Yes")
        exit()

print("No")
