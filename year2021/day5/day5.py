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
    return cross


def getNumOfPoints(myList):
    myList = correctList(myList)
    cross = getCross(myList)
    cross = fillCross(cross, myList)
    counter = 0
    for groupIndex in range(len(cross)):
        for index in range(len(cross[groupIndex])):
            if cross[groupIndex][index] >=2 :
                counter += 1
    return counter


if __name__ == '__main__':
    try:
        myList = []
        while True:
            myList.append(input())
    except:
        print(getNumOfPoints(myList))
