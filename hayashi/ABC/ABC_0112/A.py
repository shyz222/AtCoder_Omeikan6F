alp = input()
alpha2num = lambda c: ord(c) - ord('A') + 1
num2alpha = lambda c: chr(c+64)

print(num2alpha(alpha2num(alp)+1))
