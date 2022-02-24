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
    print(gamma)
    gamma.reverse()
    for i in range(len(gamma)):
        decimal = decimal + (2 ** i) * gamma[i]
    return decimal


def getEpsilonRate(list):
    for i in range(len(list)):
        list[i] = 0
        print(list[i])
    return list


try:
    myList = []
    while True:
        myList.append(input())
except:
    gamma = getGammaRate(myList)
    print('The power consumption is: ' + str(gamma * (2 ** len(myList[0]) - gamma - 1)))
