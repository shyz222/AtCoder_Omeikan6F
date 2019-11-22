s = int(input())

ans_L = []
counter = 0
tmp = 0
while True:
    
    if s%2 ==0:
        s = s/2
    else:
        s = 3*s + 1

    ans_L.append(s)

    if tmp in ans_L:
        print("------------")
        print(ans_L,s)
        print(counter)
        exit()

    tmp = s
    counter +=1