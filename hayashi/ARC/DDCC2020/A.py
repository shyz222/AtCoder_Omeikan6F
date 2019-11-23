A, B = map(int, input().split())

list = [500000,300000,200000,100000,0]

if(A>3):
    A = 4
if(B>3):
    B = 4
elif(A==1 and B==1):
    A=B=0
money = list[A]+list[B]
print(money)
