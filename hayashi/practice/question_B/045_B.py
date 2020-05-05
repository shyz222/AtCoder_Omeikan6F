card_A = input()
card_B = input()
card_C = input()

def changeTarget(target):
  ans = 'default'
  if(target == 'A'):
    ans = card_A
  elif(target == 'B'):
    ans = card_B
  elif(target == 'C'):
    ans = card_C

  return ans

target = [card_A, 'A', '']
while target[0] != '':
  if(target[0][0] == 'a'):
    target[2] = 'A'
  elif(target[0][0] == 'b'):
    target[2] = 'B'
  elif(target[0][0] == 'c'):
    target[2] = 'C'

  if(target[1] == 'A'):
    card_A = card_A[1:]
    target[1] = target[2]
    target[0] = changeTarget(target[2])
  elif(target[1] == 'B'):
    card_B = card_B[1:]
    target[1] = target[2]
    target[0] = changeTarget(target[2])
  elif(target[1] == 'C'):
    card_C = card_C[1:]
    target[1] = target[2]
    target[0] = changeTarget(target[2])

print(target[1])
