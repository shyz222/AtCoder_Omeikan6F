import itertools

N = int(input())
String_List = list(input())
#print(String_List)
total_number = 2 ** N -1

pair = len(String_List) - len(set(String_List))
if pair != 0:
    global last
    last = 2 ** (len(String_List) - 2) * pair - ((pair-1)* (len(String_List)-pair*2)*2)
else:
    last = 0

print(total_number - last　% (10**9 +7)
