""" --- Day 9: Smoke Basin --- """


def getCross(listInput):
    for index in range(len(listInput)):
        listInput[index] = list(listInput[index])
        listInput[index] = [int(x) for x in listInput[index]]
        listInput[index].insert(0, 9)
        listInput[index].insert(len(listInput[index]), 9)
    listInput.insert(0, [9 for _ in range(len(listInput[0]))])
    listInput.insert(len(listInput), [9 for _ in range(len(listInput[0]))])
    return listInput


def getSumOfTheRisk(dataIn):
    dataCross = getCross(dataIn)
    heights = []

    for rowIndex in range(1, len(dataCross) - 1):
        for colIndex in range(1, len(dataCross[rowIndex]) - 1):
            if dataCross[rowIndex][colIndex] < min(dataCross[rowIndex - 1][colIndex],
                                                   dataCross[rowIndex + 1][colIndex],
                                                   dataCross[rowIndex][colIndex - 1],
                                                   dataCross[rowIndex][colIndex + 1], ):
                heights.append(dataCross[rowIndex][colIndex])
    return sum(heights) + len(heights)


if __name__ == "__main__":
    dataFile = open('data.txt')
    dataInput = dataFile.read().split()
    print(f'Sum of the risk levels of all low points: {getSumOfTheRisk(dataInput)}')
