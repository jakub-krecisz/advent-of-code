""" --- Day 13: Transparent Origami --- """


def getCoords(dataIn):
    coords = []
    for el in dataIn:
        if len(el) == 2:
            coords.append(el)
    return coords


def toInt(coords):
    for row in range(len(coords)):
        coords[row][0] = int(coords[row][0])
        coords[row][1] = int(coords[row][1])
    return coords


def getMaxX(coords):
    maxNum = 0
    for row in coords:
        if row[0] > maxNum:
            maxNum = row[0]
    return maxNum


def getMaxY(coords):
    maxNum = 0
    for row in coords:
        if row[1] > maxNum:
            maxNum = row[1]
    return maxNum


def fillMap(map_, coordinates):
    print(map_)
    for coord in coordinates:
        print(map_[coord[0]][coord[1]])


def numOfDots(dataIn):
    dataIn = [a.split(',') for a in dataIn]
    dataIn = [a for a in dataIn if (a != ['fold']) and (a != ['along'])]
    coords = getCoords(dataIn)
    coords = toInt(coords)
    map_ = [['.' for _ in range(getMaxX(coords) + 1)] for _ in range(getMaxY(coords) + 1)]
    fillMap(map_, coords)


if __name__ == "__main__":
    dataInput = open('test_data.txt').read().split()
    print(numOfDots(dataInput))
