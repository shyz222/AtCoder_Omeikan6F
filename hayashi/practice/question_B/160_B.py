import math
X = int(input())

print((math.floor(X/500))*1000+(math.floor((X%500)/5)*5))
