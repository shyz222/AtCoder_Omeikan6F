import sys
S = sorted(set(input()))

alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(len(alp)):
  if (i>len(S)-1):
    print(alp[i])
    sys.exit()
  elif S[i] != alp[i]:
    print(alp[i])
    sys.exit()

print('None')
