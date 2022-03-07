""" --- Day 8: Seven Segment Search --- """


def getNum(data):
    data = data.split()
    uniqueDigits = [2, 3, 4, 7]
    counter = 0
    for i in range(11, len(data), 15):
        for index in range(i, i + 4):
            if len(data[index]) in uniqueDigits:
                counter += 1
    return counter


if __name__ == '__main__':
    dataFile = open('data.txt')
    dataInput = dataFile.read()
    print(getNum(dataInput))
