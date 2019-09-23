s_L = input().split(" ")


result_L = []

for a in range(0,len(s_L)):
    # 移動

    for val in range(0,len(s_L)):
        moji = s_L[a]
        jotai = moji

        if moji == "R":
            a +=1
        elif moji == "L":
            a -=1

        moji = s_L[a]

        if jotai != moji:
            point = a+val
            if point%2 == 0:
                result_L.append(point-1)
                
