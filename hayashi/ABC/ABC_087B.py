import math

A = int(input())
B = int(input())
C = int(input())
X = int(input())


amari_500 = X % 500
syou_500 = math.floor(X / 500)

if syou_500 > A:
    syou_500 = A
    amari_500 = X - (500 * syou_500)

amari_100 = amari_500 % 100
syou_100 = math.floor(amari_500 / 100)

if syou_100 > B:
    syou_100 = B
    amari_100 = amari_500 - (100 * syou_100)

amari_50 = amari_100 % 50
syou_50 = math.floor(amari_100 / 50)


if syou_50 > C:
    syou_50 = C
    amari_50 = amari_100 - (50 * syou_50)

if amari_50 != 0:
    ans = 0
else:
