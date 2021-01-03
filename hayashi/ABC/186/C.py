N = int(input())


def is_seven(number):
    return "7" in str(number)


ans_count = 0
for i in range(1, N+1):
    if not (is_seven(i) or is_seven(oct(i))):
        ans_count += 1

print(ans_count)
