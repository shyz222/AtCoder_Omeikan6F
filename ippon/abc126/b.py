s = list(input())
YYMM = 0
MMYY = 0
if 1 <= int(s[2]+s[3]) <= 12:
    YYMM = 1
if 1 <= int(s[0]+s[1]) <= 12:
    MMYY = 1
 
if MMYY == YYMM == 1:
    print("AMBIGUOUS")
elif YYMM == 1:
    print("YYMM")
elif MMYY == 1:
    print("MMYY")
else:
    print("NA")
