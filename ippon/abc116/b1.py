s = int(input())
 
t = [False] * 1000001
i = 1
while True:
  if s <= 1000000 and t[s] == True:
    break
  t[s] = True
  i += 1
  if s % 2 == 0:
    s = s // 2
  else:
    s = 3 * s + 1
 
print(i)