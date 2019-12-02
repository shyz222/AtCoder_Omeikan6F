a,b = map(int,input().split())

kigo = ["+","-","*"]
s_L = []
for val in kigo:
    tmp = eval(str(a) + val + str(b))
    s_L.append(tmp)
print(max(s_L))