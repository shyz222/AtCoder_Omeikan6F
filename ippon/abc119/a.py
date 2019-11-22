s = input()
year,month,day = map(int,s.split("/"))

if year < 2019:
    print("Heisei")
    exit()
if month < 5:
    print("Heisei")
    exit()

print("TBD")
