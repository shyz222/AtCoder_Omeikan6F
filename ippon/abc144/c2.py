import math
#試し割法
def trial_division(n):
    #素因数を格納するリスト
    factor = []
    #2から√n以下の数字で割っていく
    tmp = int(math.sqrt(n)) + 1
    for num in range(2,tmp):
        while n % num == 0:
            n //= num
            factor.append(num)
    if not factor:
        return n
    else:
        factor.append(n)
        return factor

if __name__=="__main__":
    n = int(input())
    