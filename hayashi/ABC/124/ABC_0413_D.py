N , K = map(int, input().split())
list_input = list(map(int, input()))

list = []
sameColorList = []

for i in range(len(list_input)):
    if len(list_input)-i =1:
        if list_input[i] !=
    elif list_input[i] == list_input[i+1] and list_input[i+1] != list_input[i+2]:
        sameColorList.append(list_input[i])
        sameColorList.append(list_input[i+1])
        list.append(sameColorList)
        sameColorList = []
    elif list_input[i] == list_input[i+1] and list_input[i+1] == list_input[i+2]:
        sameColorList.append(list_input[i])

print(list)
