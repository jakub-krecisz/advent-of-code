""" --- Day 4: Giant Squid --- """

def getBingoList(myList):
    correctedList = []
    for i in range(1, len(myList)):
        correctedList.append(myList[i].split())

    return correctedList



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
    print(bingoList)
    counter = [[] for _ in range(len(bingoList)*5)]
    for groupIndex in range(len(bingoList)):
        for number in numbers:
            for index in range(len(bingoList[groupIndex])):
                if number in bingoList[groupIndex][index]:
                    counter[index].append(number)
                    if len(counter[index]) == 5:
                        return int(getResult(counter, bingoList[groupIndex])) * int(number)



try:
    myList = []
    while True:
        myList.append(input())
except:
    print(f'Final score is: {getScore(myList)}')