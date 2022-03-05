def correctList(list):
    correctedList = []
    for el in list:
        coords = el[:el.find(' -> ')].split(',') + el[el.find(' -> ') + 4:].split(',')
        correctedList.append(coords)
    for groupIndex in range(len(correctedList)):
        for index in range(len(correctedList[groupIndex])):
            correctedList[groupIndex][index] = int(correctedList[groupIndex][index])
    return correctedList


def getCross(list):
    x, y = 0, 0
    for el in list:
        if x < max(el[0], el[2]):
            x = max(el[0], el[2])
        if y < max(el[1], el[3]):
            y = max(el[1], el[3])
    cross = [[0 for _ in range(x + 1)] for _ in range(y + 1)]
    return cross


def fillCross(cross, coords):
    for coordinate in coords:
        if coordinate[0] == coordinate[2]:
            for yIndex in range(min(coordinate[1], coordinate[3]), max(coordinate[1], coordinate[3]) + 1):
                cross[yIndex][coordinate[0]] += 1
        elif coordinate[1] == coordinate[3]:
            for xIndex in range(min(coordinate[0], coordinate[2]), max(coordinate[0], coordinate[2]) + 1):
                cross[coordinate[1]][xIndex] += 1
        elif coordinate[0] == coordinate[1] and coordinate[2] == coordinate[3]:
            for coord in range(min(coordinate[0], coordinate[2]), max(coordinate[0], coordinate[2] + 1)):
                cross[coord][coord] += 1
        elif coordinate[0] == coordinate[3] and coordinate[1] == coordinate[2]:
            y = max(coordinate[0], coordinate[1])
            for x in range(min(coordinate[0], coordinate[1]), y + 1):
                cross[y][x] += 1
                y -= 1
        elif coordinate[0] - coordinate[2] == coordinate[1] - coordinate[3]:
            x = min(coordinate[0], coordinate[2])
            y = min(coordinate[1], coordinate[3])
            for xCoord in range(x, max(coordinate[0], coordinate[2]) + 1):
                cross[y][xCoord] += 1
                y += 1
        elif abs(coordinate[0] - coordinate[2]) == coordinate[1] - coordinate[3]:
            y = coordinate[1]
            for xCoord in range(coordinate[0], coordinate[2] + 1):
                cross[y][xCoord] += 1
                y -= 1
        elif coordinate[0] - coordinate[2] == abs(coordinate[1] - coordinate[3]):
            x = coordinate[0]
            for yCoord in range(coordinate[1], coordinate[3] + 1):
                cross[yCoord][x] += 1
                x -= 1
    return cross


def getNumOfPoints(myList):
    myList = correctList(myList)
    cross = getCross(myList)
    cross = fillCross(cross, myList)
    """ uncomment if u want to see diagram """
    # for el in cross:
    #     for ell in el:
    #         if ell != 0:
    #             print(ell, end='')
    #         else:
    #             print('.', end='')
    #     print()
    counter = 0
    for groupIndex in range(len(cross)):
        for index in range(len(cross[groupIndex])):
            if cross[groupIndex][index] >= 2:
                counter += 1
    return counter


if __name__ == '__main__':
    try:
        myList = []
        while True:
            myList.append(input())
    except:
        print(f'The number of points is: {getNumOfPoints(myList)}')
