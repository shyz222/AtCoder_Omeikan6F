
j = input()
k = int(input())

j = j*k

counter = 0
ans_L = []

s = [i for i in j]
s.append("0")
renzoku = 1

for val in range(0,len(s)-1):
    tmp = s[val+1]
    if s[val] == tmp:
        renzoku += 1
    elif renzoku > 1 and s[val] != tmp:
        ans_L.append(renzoku//2)
        renzoku = 1
print(sum(ans_L))
