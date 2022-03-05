""" --- Day 4: Giant Squid --- """


def getBingoList(myList):
    correctedList = []
    for i in range(1, len(myList)):
        correctedList.append(myList[i].split())
        finalList = []
        list = []
    for index in range(len(correctedList)):
        if index % 6 == 0:
            finalList.append(list)
            list.clear()
        list.append(correctedList[index])
    return finalList


def getResult(wonList, bingoList):
    result = 0
    wonList = correctList(wonList)
    bingoList = correctList(bingoList)
    for bingoListEl in bingoList:
        if bingoListEl not in wonList:
            result += int(bingoListEl)
    return result


def correctList(list):
    correctedList = []
    for el in list:
        correctedList += el
    return correctedList


def getScore(myList):
    numbers = myList[0].split(',')
    myList.remove('')
    bingoList = getBingoList(myList)
    counter = [[[], [], [], [], []] for _ in range(len(bingoList))]
    for number in numbers:
        for groupIndex in range(len(bingoList[0])):
            for index in range(len(bingoList[groupIndex])):
                if number in bingoList[groupIndex][index]:
                    counter[groupIndex][index].append(number)
                    if len(counter[groupIndex][index]) == 5:
                        return int(getResult(counter[groupIndex], bingoList[groupIndex])) * int(number)


if __name__ == '__main__':
    try:
        myList = []
        while True:
            myList.append(input())
    except:
        print(f'Final score is: {getScore(myList)}')
