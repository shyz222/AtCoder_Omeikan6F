
n = int(input())
s = input()
# 26(25)
tmp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

a_L = [val for val in tmp]
ans = ""
for val in s:
    i = a_L.index(val)
   
    if i+n >= 26:
        aa = i+n - 26
        #print("aaaa") 
    else:
        aa = i + n
    #print(aa)
    ans += a_L[aa]
print(ans)
#a,b = map(int,input().split())
#a_L = map(int,input().split())

