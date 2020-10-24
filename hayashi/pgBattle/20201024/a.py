N = int(input())

ans = N
for i in range(N):
    key = input()
    if key == "AC":
        ans -= 1
    
print(ans * 5)