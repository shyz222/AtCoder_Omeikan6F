H, W = map(int, input().split())
px, py, qx, qy = map(int, input().split())

mapList = []
routeList = []

for height in H:
    _list = list(map(int, input().split()))
    mapList.append(_list)

currentLocation = [px, py, 0]

def checkTarget(currentHead) {
    if currentHead == 0:
        return [0, 1]
    elif currentHead == 90:
        return [-1, 0]
    elif currentHead == 180:
        return [0, -1]
    else:
        return [1, 0]
}

while (currentLocation[0] != qx or currentLocation[1] != qy) and (currentLocation not in routeList):
    routeList.append(currentLocation)
    target = ""
    turn = 0
    while target != "." and turn != 4:
        head = currentLocation[3]
        if (head == 270):
            head = 0
        else:
            head += 90
        turn += 1
        target = [currentLocation[0], currentLocation[1]] - checkTarget(head)
        

