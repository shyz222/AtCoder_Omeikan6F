N = int(input())
input_list = list(map(int, input().split()))

count = 0


def by2(int):
    return int/2


all_even_flag = all(i % 2 == 0 for i in input_list)

while all_even_flag == True:
    input_list = list(map(by2, input_list))
    count += 1
    all_even_flag = all(i % 2 == 0 for i in input_list)

print(count)
