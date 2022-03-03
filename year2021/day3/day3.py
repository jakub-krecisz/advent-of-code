""" --- Day 3: Binary Diagnostic --- """


def getGammaRate(myList):
    gamma = [0 for _ in range(len(myList[0]))]
    decimal = 0
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
    gamma.reverse()
    for i in range(len(gamma)):
        decimal = decimal + (2 ** i) * gamma[i]
    return decimal


def getOxygenRate(myList):
    oxygen = [0 for _ in range(len(myList[0]))]
    decimal = 0
    for element in myList:
        for i in range(len(myList[0])):
            if element[i] == '0':
                oxygen[i] -= 1
            else:
                oxygen[i] += 1
    print(oxygen)

    for index in range(len(oxygen)):
        if oxygen[index] >= 0:
            oxygen[index] = 1
        else:
            oxygen[index] = 0
    print(oxygen)
    oxygen.reverse()
    for i in range(len(oxygen)):
        decimal = decimal + (2 ** i) * oxygen[i]
    return decimal


if __name__ == '__main__':
    try:
        myList = []
        while True:
            myList.append(input())
    except:
        gamma = getGammaRate(myList)
        """ ---- PART ONE ---- """
        print('The power consumption is: ' + str(gamma * (2 ** len(myList[0]) - gamma - 1)))

        """ ---- PART TWO ---- """
        print('Oxygen generator rate is: ' + str(getOxygenRate(myList)))
