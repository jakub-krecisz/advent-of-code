""" --- Day 4: Giant Squid --- """

def getBingoList(myList):
    correctedList = []
    for i in range(1, len(myList)):
        correctedList.append(myList[i].split())
    return correctedList

def getScore(myList):
    numbers = myList[0].split(',')
    myList.remove('')
    bingoList = getBingoList(myList)
    print('ok')


try:
    myList = []
    while True:
        myList.append(input())
except:
    getScore(myList)