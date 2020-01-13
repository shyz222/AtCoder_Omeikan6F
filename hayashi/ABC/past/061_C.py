def dfs(i, f):
    if i == n - 1:
        return sum(list(map(int, f.split("+"))))
        # return sum(list(map(eval,f)))

    # 式 f の末尾に "+" を追加するかしないかして次の数字を追加
    return dfs(i + 1, f + s[i+1])+ dfs(i + 1, f + "+" + s[i + 1])


s = input()
n = len(s)

print(dfs(0, s[0]))
