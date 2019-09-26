input()
N=eval(input().replace(' ','|'))
print(len(bin((N&-N)))-3)
