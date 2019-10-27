s_L = [str(val) for val in input()]
n = len(s_L)

p_1,p_2 = [],[]
for val in range(n):
    if val%2 ==0:
        p_1.append("0")
        p_2.append("1")
    else:
        p_1.append("1")
        p_2.append("0")
counter1,counter2 = 0,0

for val in range(n):
    if p_1[val] == s_L[val]:
        counter1 +=1
    else:
        counter2 +=1
print(min(counter1,counter2))
