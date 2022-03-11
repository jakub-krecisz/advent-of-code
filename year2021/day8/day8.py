""" --- Day 8: Seven Segment Search --- """


def getTopWord(twoLen, threeLen):
    twoLenList, threeLenList = list(twoLen[0]), list(threeLen[0])
    for el in threeLenList:
        if el not in twoLenList:
            return el


def getRightTopWord(twoLen, sixLen):
    twoLenList = list(twoLen[0])
    for el in sixLen:
        if twoLenList[0] not in list(el):
            return twoLenList[0]
        elif twoLenList[1] not in list(el):
            return twoLenList[1]

def getRightBottomWord(twoLen, sixLen):
    twoLenList = list(twoLen[0])
    for el in sixLen:
        if twoLenList[0] not in list(el):
            return twoLenList[1]
        elif twoLenList[1] not in list(el):
            return twoLenList[0]


def getValue(data):
    numLen = {
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
    }
    display = {}
    for index in range(10):
        for length in range(2, 8):
            if int(len(data[index])) == length:
                numLen[length].append(data[index])
    display[0] = getTopWord(numLen[2], numLen[3])
    display[2] = getRightTopWord(numLen[2], numLen[6])
    display[5] = getRightBottomWord(numLen[2], numLen[6])
    print(display)
    print(numLen)
    return 0


def separateData(data):
    data = data.split()
    separatedList = []
    for i in range(0, len(data), 15):
        separatedList.append([])
        for index in range(i, i + 15):
            separatedList[i // 15].append(data[index])
    return separatedList


def getSum(data):
    data = separateData(data)
    total = 0
    for el in data:
        total += getValue(el)
    return data


def getNum(data):
    data = data.split()
    uniqueDigits = [2, 3, 4, 7]
    counter = 0
    for i in range(11, len(data), 15):
        for index in range(i, i + 4):
            if len(data[index]) in uniqueDigits:
                counter += 1
    return counter


if __name__ == '__main__':
    dataFile = open('data.txt')
    dataInput = dataFile.read()
    print(getNum(dataInput))
    print(getSum(dataInput))
