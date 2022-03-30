""" --- Day 13: Transparent Origami --- """


def getCoords(dataIn):
    coords = []
    for el in dataIn:
        if len(el) == 2:
            coords.append(el)
    for row in range(len(coords)):
        coords[row][0] = int(coords[row][0])
        coords[row][1] = int(coords[row][1])
    return coords


def getFolds(dataIn):
    folds = []
    for index in range(len(dataIn) - 1, 0, -1):
        if len(dataIn[index]) == 1:
            folds.append(dataIn[index][0])
        else:
            return folds[::-1]


def doYFold(map_, fold):
    folded = []
    for row in range(int(fold[2:]) + 1, len(map_)):
        folded.append(map_[row])

    for row in range(len(folded)):
        for col in range(len(folded[row])):
            if folded[::-1][row][col] != map_[row][col]:
                folded[::-1][row][col] = '#'
    return folded[::-1]


def doXFold(map_, fold):
    folded = []
    for row in map_:
        folded.append(row[int(fold[-1]) + 1:])
    folded = [row[::-1] for row in folded]
    for row in range(len(folded)):
        for col in range(len(folded[row])):
            if folded[row][col] != map_[row][col]:
                folded[row][col] = '#'
    return folded


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
    for coord in coordinates:
        map_[coord[1]][coord[0]] = '#'
    return map_


def numOfDots(dataIn):
    dataIn = [a.split(',') for a in dataIn]
    dataIn = [a for a in dataIn if (a != ['fold']) and (a != ['along'])]
    coords = getCoords(dataIn)
    folds = getFolds(dataIn)
    map_ = [['.' for _ in range(getMaxX(coords) + 1)] for _ in range(getMaxY(coords) + 1)]
    map_ = fillMap(map_, coords)
    # for fold in folds:
    #     if fold[:1] == 'y':
    #         map_ = doYFold(map_, fold)
    #     else:
    #         map_ = doXFold(map_, fold)
    map_ = doYFold(map_, folds[0])
    counter = 0
    for row in range(len(map_)):
        for col in range(len(map_[row])):
            if map_[row][col] == '#':
                counter += 1
    return counter


if __name__ == "__main__":
    dataInput = open('data.txt').read().split()
    print(numOfDots(dataInput))
