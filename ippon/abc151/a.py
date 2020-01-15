#n = int(input())
#a_L = map(int,input().split())
s  = input()
L = [chr(ord('a') + i) for i in range(26)]

print(L[L.index(s)+1])
