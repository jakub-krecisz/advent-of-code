""" --- Day 3: Binary Diagnostic --- """


def getGammaRate(myList):
    gamma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
    return ''.join(str(gamma))


try:
    myList = []
    while True:
        myList.append(input())
except:
    print(getGammaRate(myList))
