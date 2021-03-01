S = input()

# array_a = []
# array_b = []
# array_c = []

# for char in S:
#     if char == "a":
#         array_a.append(char)
#         continue
#     if char == "b":
#         array_b.append(char)
#         continue
#     if char == "c":
#         array_c.append(char)
#         continue

# max_len = max(len(array_a), len(array_b), len(array_c))

# if max_len == len(array_a):
#     print("a")
# elif max_len == len(array_b):
#     print("b")
# else:
#     print("c")

# 模範回答

count_a = S.count("a")
count_b = S.count("b")
count_c = S.count("c")

largest = max(count_a, count_b, count_c)

if largest == count_a:
    print("a")
elif largest == count_b:
    print("b")
else:
    print("c")
