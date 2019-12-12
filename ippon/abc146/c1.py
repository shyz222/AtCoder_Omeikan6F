a,b,x = map(int,input().split())

left,right = 0,10**9+1

# if x > a * right + b*len(str(right)):
#     print(0)
#     exit()

while right - left > 1:
    mid = (right + left)//2
    mid_p = a * mid + b*len(str(mid))

    if mid_p <= x:
        left = mid
    else:
        right = mid


print(left)
