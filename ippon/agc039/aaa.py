j = input()
k = int(input())
 
 
 
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
 
 
 
# 繋がっている場合
# kbk
renzoku = 0
if s[0] == s[-2]:
    for val in range(len(s)+1):
        if s[val+1] == s[0]:
            renzoku += 1
        else:
            break
 
if len(s) == 2:
    print(k//2)
    import sys
    sys.exit()
    
    
 
print(sum(ans_L)*k + renzoku%2)
