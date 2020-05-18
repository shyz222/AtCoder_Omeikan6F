N = int(input())
str = input()
count = N
z = 0
for i in str:
    if(z == N-1):
        break
    elif(i == str[z+1]):
        count -= 1
    z += 1
print(count)
