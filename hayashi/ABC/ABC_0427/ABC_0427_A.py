import math

A, B, T = map(int, input().split())

bisket = math.floor((T / A)) * B

print(bisket)
