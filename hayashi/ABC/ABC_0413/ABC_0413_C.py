list_input = list(map(int, input()))

len_val = len(list_input)
ans_a = []
ans_b = []

a_count = 0
b_count = 0

for i in range(len_val):

    ans_a.append(i%2)
    ans_b.append((i+1)%2)

for i in range(len_val):
    if ans_a[i] == list_input[i]:
        b_count += 1
    else:
        a_count += 1

if a_count >= b_count:
    print(b_count)
else:
    print(a_count)
