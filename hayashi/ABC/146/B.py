N = int(input())
S = input()

alpha2num = lambda c: ord(c) - ord('A') + 1
num2alpha = lambda c: chr(c+64)
list = []
for i in S:
    number = alpha2num(i)
    number_after = number + N
    if number_after > 26:
        number_after = number_after - 26
    i = num2alpha(number_after)
    list.append(i)

print(''.join(list))
