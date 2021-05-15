a = input()

index = a.find(".")

ans = a[:index]

if index == -1:
    ans = a
print(ans)
