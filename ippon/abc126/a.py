n,k= map(int,input().split())
s = input()

s = [val for val in s]

s[k-1]=s[k-1].lower()

print("".join(s))
