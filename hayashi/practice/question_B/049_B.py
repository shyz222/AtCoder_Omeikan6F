H, W = map(int, input().split())

ans = []
for i in range(H):
  pixels = input()
  for i in range(2):
    ans.append(pixels)

for i in range(len(ans)):
  print(ans[i])
