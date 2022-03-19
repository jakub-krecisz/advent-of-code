""" --- Day 11: Dumbo Octopus --- """


def inRange(matrix, x, y):
    if x < 0 or y < 0:
        return False
    if (x >= len(matrix)) or (y >= len(matrix[x])):
        return False
    return True


def incrementSurroundings(matrix, rowIndex, colIndex):
    for j in [-1, 0, 1]:
        for i in [-1, 0, 1]:
            newRowIndex = rowIndex + j
            newColIndex = colIndex + i
            if inRange(matrix, newRowIndex, newColIndex) and matrix[newRowIndex][newColIndex] != 0:
                matrix[newRowIndex][newColIndex] += 1


def startStep(matrix):
    for rowCounter in range(len(matrix)):
        for colCounter in range(len(matrix[rowCounter])):
            matrix[rowCounter][colCounter] = matrix[rowCounter][colCounter] + 1
    return doFlashes(matrix)


def doFlashes(matrix):
    changeCounter = 0
    haveChangesOccured = False
    listToIncrement = []
    for rowCounter in range(len(matrix)):
        for colCounter in range(len(matrix[rowCounter])):
            if matrix[rowCounter][colCounter] > 9:
                listToIncrement.append((rowCounter, colCounter))
                matrix[rowCounter][colCounter] = 0
                changeCounter += 1
                haveChangesOccured = True
    if haveChangesOccured:
        for (i, j) in listToIncrement:
            incrementSurroundings(matrix, i, j)
        return changeCounter + doFlashes(matrix)
    else:
        return changeCounter


def getMatrix(fileName):
    matrix = []
    with open(fileName) as f:
        for line in f:
            matrix.append(list(line))
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == '\n':
                matrix[row].pop()
            else:
                matrix[row][col] = int(matrix[row][col])
    return matrix


def getTotalFlashes(matrix):
    changeCounter = 0
    for i in range(100):
        changeCounter += startStep(matrix)
    return changeCounter


if __name__ == "__main__":
    # Part One
    print(f'Total flashes after 100 steps: {getTotalFlashes(getMatrix("data.txt"))}')
