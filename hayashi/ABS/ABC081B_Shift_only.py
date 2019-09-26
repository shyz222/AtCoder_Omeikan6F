N = input()
A_list = [int(s) for s in input().split()]
def even(n):
    return n % 2
def harf(n):
    return n / 2
amari = sum(list(map(even, A_list)))
count = 0
while amari == 0:
    A_list = list((map(harf, A_list)))
    count +=1
    amari = sum(list(map(even, A_list)))
print(count)
