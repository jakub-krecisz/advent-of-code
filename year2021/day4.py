""" --- Day 4: Giant Squid --- """

def getBingoList(myList):
    correctedList = []
    for i in range(1, len(myList)):
        correctedList.append(myList[i].split())
    correctedList.remove([])
    correctedList.remove([])
    return correctedList

def getScore(myList):
    numbers = myList[0].split(',')
    myList.remove('')
    bingoList = getBingoList(myList)
    counter = [0 for _ in range(len(bingoList))]
    for number in numbers:
        for index in range(len(bingoList)):
            if number in bingoList[index]:
                counter[index] += 1
                if counter[index] == 5:
                    return bingoList[index]


try:
    myList = []
    while True:
        myList.append(input())
except:
    print(getScore(myList))