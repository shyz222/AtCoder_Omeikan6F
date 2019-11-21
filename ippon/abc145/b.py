n = int(input())
s_ = input()
s = [val for val in s_]

if n % 2 !=0:
    print("No")
else:
    tmp = int(len(s)/2)

    if s[0:tmp] == s[tmp:]:
        print("Yes")
    else:
        print("No")