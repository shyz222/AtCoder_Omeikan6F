import sys
s = input()

s = [val for val in s]
s.sort()

a = set(s)
if len(a) != 2:
    print("No")
    sys.exit()
if s[1] != s[2]:
    print("Yes")
else:
    print("No")


