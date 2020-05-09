N = input()
ans = ''
for i in range(len(N)):
  if(ans == '' and N[i] == "B"):
    pass
  elif(ans == '' and N[i] != "B"):
    ans = N[i]
  elif(N[i] == "B"):
    ans = ans[:-1]
  else:
    ans += N[i]

print(ans)
