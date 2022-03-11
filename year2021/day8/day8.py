""" --- Day 8: Seven Segment Search --- """

def getKey(value, dataTuple):
    for key, val in dataTuple.items():
        if val == value:
            return key

def getTopWord(twoLen, threeLen):
    twoLenList, threeLenList = list(twoLen[0]), list(threeLen[0])
    for el in threeLenList:
        if el not in twoLenList:
            return el


def getTopLeftWord(twoLen, fourLen, fiveLen):
    filtered = []
    for el in list(fourLen):
        if el not in list(twoLen):
            filtered.append(el)
    for el in fiveLen:
        if filtered[0] not in list(el):
            return filtered[0]
        elif filtered[1] not in list(el):
            return filtered[1]


def getRightTopWord(twoLen, sixLen):
    twoLenList = list(twoLen[0])
    for el in sixLen:
        if twoLenList[0] not in list(el):
            return twoLenList[0]
        elif twoLenList[1] not in list(el):
            return twoLenList[1]


def getCenterWord(twoLen, fourLen, fiveLen):
    filtered = []
    for el in list(fourLen):
        if el not in list(twoLen):
            filtered.append(el)
    for el in fiveLen:
        if filtered[0] not in list(el):
            return filtered[1]
        elif filtered[1] not in list(el):
            return filtered[0]


def getLeftBottomWord(display, sixLen, centerWord):
    filtered = []
    for el in sixLen:
        if centerWord not in list(el):
            for word in list(el):
                if word not in display.values():
                    filtered.append(word)
    for el in sixLen:
        if filtered[0] not in list(el):
            return filtered[0]
        elif filtered[1] not in list(el):
            return filtered[1]


def getRightBottomWord(twoLen, sixLen):
    twoLenList = list(twoLen[0])
    for el in sixLen:
        if twoLenList[0] not in list(el):
            return twoLenList[1]
        elif twoLenList[1] not in list(el):
            return twoLenList[0]


def getBottomWord(display, sixLen, centerWord):
    filtered = []
    for el in sixLen:
        if centerWord not in list(el):
            for word in list(el):
                if word not in display.values():
                    filtered.append(word)
    for el in sixLen:
        for word in list(el):
            if word not in display.values():
                return word


def getValueFromStr(value, display):
    numbers = {
        1: [display[2], display[5]],
        2: [display[0], display[2], display[3], display[4], display[6]],
        3: [display[0], display[2], display[3], display[5], display[6]],
        4: [display[1], display[2], display[3], display[5]],
        5: [display[0], display[1], display[3], display[5], display[6]],
        6: [display[0], display[1], display[3], display[4], display[5], display[6]],
        7: [display[0], display[2], display[5]],
        8: [display[i] for i in range(7)],
        9: [display[0], display[1], display[2], display[3], display[5], display[6]],
        0: [display[0], display[1], display[2], display[4], display[5], display[6]]
    }

    for val in numbers.values():
        if all(word in val for word in list(value)):
            if all(word in list(value) for word in val):
                return getKey(val, numbers)


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
    summary = 0
    for index in range(10):
        for length in range(2, 8):
            if int(len(data[index])) == length:
                numLen[length].append(data[index])
    display[0] = getTopWord(numLen[2], numLen[3])
    display[1] = getTopLeftWord(numLen[2][0], numLen[4][0], numLen[5])
    display[2] = getRightTopWord(numLen[2], numLen[6])
    display[3] = getCenterWord(numLen[2][0], numLen[4][0], numLen[5])
    display[5] = getRightBottomWord(numLen[2], numLen[6])
    display[4] = getLeftBottomWord(display, numLen[6], display[3])
    display[6] = getBottomWord(display, numLen[6], display[3])
    for index in range(11, 15):
        summary += getValueFromStr(data[index], display)
    return summary


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
        print(getValue(el))
    return total


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
    print(f'How many times numbers appear: {getNum(dataInput)}')
    print(getSum(dataInput))