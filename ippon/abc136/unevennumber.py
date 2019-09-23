n = input()

counter = 0
for val in range(1,int(n)+1):
    if len(str(val))%2 != 0:
        counter +=1

print(counter)
