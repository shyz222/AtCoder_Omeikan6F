def is_match(T, S):
    for i in range(len(S) - len(T) + 1):
        flag = True
        for j in range(len(T)):
            if T[j] == "." or S[i+j] == T[j]:
                continue
            else:
                flag = False
        if flag:
            return True
    return False


char = "abcdefghijklmnopqrstuvwxyz."

S = input()

ans = 0
for i in range(min(3, len(S))):
    T = ""
    if i == 0:
        for t in char:
            T = t
            if is_match(T, S):
                ans += 1
    elif i == 1:
        for t1 in char:
            for t2 in char:
                T = t1 + t2
                if is_match(T, S):
                    ans += 1
    elif i == 2:
        for t1 in char:
            for t2 in char:
                for t3 in char:
                    T = t1 + t2 + t3
                    if is_match(T, S):
                        ans += 1

print(ans)
