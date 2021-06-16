X = int(input())

# stock = 0
# if X < 100:
#     stock = X
# else:
#     X_2 = str(X)[-2:]
#     int_X_2 = int(X_2)
#     stock = int_X_2

# print(100-stock)

print(100-(X % 100))
