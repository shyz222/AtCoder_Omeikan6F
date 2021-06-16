S = input()

num_min = 1000
for i in range(len(S)-2):
    num = S[i:i+3]
    num_min = min(num_min, abs(753 - int(num)))

print(num_min)
