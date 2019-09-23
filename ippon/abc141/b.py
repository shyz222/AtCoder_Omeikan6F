import sys

s = input()

rud1 = ["R","U","D"]
lud2 = ["L","U","D"]


for val in range(0,len(s),2):
    if s[val] not in rud1:
        print("No")
        sys.exit(0)

for val in range(1,len(s),2):
    if s[val] not in lud2:
        print("No")
        sys.exit(0)
print("Yes")
