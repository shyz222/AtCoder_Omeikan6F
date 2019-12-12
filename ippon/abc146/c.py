#n = input()
#n = int(input())
a,b,x = map(int,input().split())
#a_L = map(int,input().split())

#s_L = list(range(1,x))

# binary search
if a  + b > x:
    print(0)
    exit()

n1,n2 = 1,10**9
n1_L,n2_L = [],[]


while n2 - n1 > 2:

    n1_price = a * n1 + b * len(str(n1))
    n2_price = a * n2 + b * len(str(n2))
    
    n1_L.append(n1)
    n2_L.append(n2)

    """
    if n1_price <= x and n2_price > x:
        n2 = int((n2-n1)/2)
        #n2_L.append(n2)
        #n1 = (n2 - n1)/2
    elif n1_price <=x and n2_price <=x:
        n1 = n2
        n2 = n2_L[-1]

    elif n1_price > x and n2_price > x:
        n1 = n1_L[-1]
        n2 = n1
    """
    if n2_price > x:
        n2 = int((n1 + n2)/2)
        #print(n2)
    if n2_price < x:
        n1 = n2
        n2 = n2_L[-1]
 
    #print(n1,n2)

print(n2)

#print(1000000000)
#print(n1_price,n2_price)
