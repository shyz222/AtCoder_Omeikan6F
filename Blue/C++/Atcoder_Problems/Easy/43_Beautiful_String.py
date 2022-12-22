w = str(input())
ws = []
for i in w:
  if i in ws and len(w) != 0:
    ws.remove(i)
  else:
    ws.append(i)

if len(ws) == 0:
  print("Yes")
else:
  print("No")