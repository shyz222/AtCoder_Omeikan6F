import copy

s = list(input())
s_t = copy.deepcopy(s)
##if s[0] =="A" and "C" in s[2:-2]:
#    if
counter = 0
 
if s[0] != "A":
    print("WA")
    exit()
 
if not "C" in s[2:-1]:
    print("WA")
    exit()
 

c = False
komojo = True

for i in range(len(s)):
    if  2 <= i <= len(s)-2:
        if s[i] == "C":
            if c == True:
                print("WA")
                exit()
            elif c != True:
                c = True
            #continue
        elif not s[i].islower():
            komojo = False
    elif i != 0 and not s[i].islower():
        komojo = False
        

if c and komojo:
    print("AC")
else:
    print("WA")


