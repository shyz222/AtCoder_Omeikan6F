import sys

w = input()
dict = {}
keys = []
value = []
for i in range(len(w)):
  if(w[i] not in keys):
    keys.append(w[i])

for i in range(len(keys)):
  value.append(w.count(keys[i]))
  if(value[i] % 2 != 0):
    print('No')
    sys.exit()

print('Yes')
