from collections import deque
s = input()
a_L = deque([val for val in s])

div_L = [""]
moji = ""

counter = 0

while a_L:
    tmp = a_L.popleft()
    moji += tmp
    if moji !=  div_L[counter]:
        div_L.append(moji)
        moji = ""
        counter += 1

print(len(div_L)-1)
