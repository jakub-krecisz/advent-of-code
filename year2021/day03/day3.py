""" --- Day 3: Binary Diagnostic --- """


def binToDeci(binary):
    return sum(val * (2 ** idx) for idx, val in enumerate(reversed(binary)))


def correctList(dataIn):
    for index in range(len(dataIn)):
        dataIn[index] = list(dataIn[index])
        dataIn[index] = [int(x) for x in dataIn[index]]
    return dataIn


def checkBitOxygen(bitIndex, myList):
    if len(myList) == 1:
        return myList
    else:
        valList = []
        remainRows = []
        for row in myList:
            valList.append(row[bitIndex])
        if valList.count(0) > valList.count(1):
            for row in myList:
                if row[bitIndex] == 0:
                    remainRows.append(row)
        else:
            for row in myList:
                if row[bitIndex] == 1:
                    remainRows.append(row)
        return remainRows


def checkBitScrubber(bitIndex, myList):
    if len(myList) == 1:
        return myList
    else:
        valList = []
        remainRows = []
        for row in myList:
            valList.append(row[bitIndex])
        if valList.count(0) <= valList.count(1):
            for row in myList:
                if row[bitIndex] == 0:
                    remainRows.append(row)
        else:
            for row in myList:
                if row[bitIndex] == 1:
                    remainRows.append(row)
        return remainRows

def getGammaRate(myList):
    gamma = [0 for _ in range(len(myList[0]))]
    for element in myList:
        for i in range(len(myList[0])):
            if element[i] == '0':
                gamma[i] -= 1
            else:
                gamma[i] += 1
    for index in range(len(gamma)):
        if gamma[index] <= 0:
            gamma[index] = 0
        else:
            gamma[index] = 1

    return binToDeci(gamma)


def getScrubberRating(myList):
    myList = correctList(myList)
    for i in range(len(myList[0])):
        myList = checkBitScrubber(i, myList)
    print(myList)
    return binToDeci(myList[0])


def getOxygenRate(myList):
    myList = correctList(myList)
    for i in range(len(myList[0])):
        myList = checkBitOxygen(i, myList)
    return binToDeci(myList[0])


if __name__ == '__main__':
    dataFile = open('data.txt')
    dataInput = dataFile.read().split('\n')

    # Part one
    print('The power consumption is: ' + str(getGammaRate(dataInput) * (2 ** len(dataInput[0])
                                                                        - getGammaRate(dataInput) - 1)))
    # Part two
    print('Life support rating is: ' + str(getOxygenRate(dataInput) * getScrubberRating(dataInput)))
