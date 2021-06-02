S = list(input())

ans = []

for i in S[::-1]:
    if i == "6":
        i = "9"
    elif i == "9":
        i = "6"
    ans.append(i)

print("".join(ans))
