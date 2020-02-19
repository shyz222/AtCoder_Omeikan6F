H, N = map(int, input().split())
a = [0] * N
b = [0] * N
x = [0] * N
for i in range(N):
    a[i], b[i]  = map(int, input().split())
    x[i] = a[i]/b[i]

xMaxIndex = x.index(max(x))
Last = H%a[xMaxIndex]
MP_NOW = b[xMaxIndex] * (H//a[xMaxIndex])

for n in range(len(a)):
  if(a[n] < H):
    b[n] = b[n] * (-(-H//a[n]))

BMinIndex = b.index(min(b))
count = -(-Last//a[BMinIndex])
print(MP_NOW + (b[BMinIndex] * count))

while H > 0:
    if(a[n] < H):
      b[n] = b[n] * (-(-Last//a[n]))
      BMinIndex = b.index(min(b))
      count = -(-Last//a[BMinIndex])
    H = H%a[BMinIndex]
    MP_NOW += b[BMinIndex] * (H//a[BMinIndex])

print(MP_NOW)
