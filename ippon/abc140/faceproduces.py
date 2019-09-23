n,k = input().split()
tmp = input()


s = []
for val in tmp:
    if val == "L":
        s.append(1)
    else:
        s.append(-1)

goukei = 10**5

for w in range(2,int(n)):
    for i in s:
        try:
            tmp = sum(s[i:i+w])
        except:
            pass
        if tmp < goukei:
            goukei = tmp
            haba = w
            index = i

new = []
for val in s[index:w]:
    new.append(int(val)*-1)

s[index:w] = new
print(s)
