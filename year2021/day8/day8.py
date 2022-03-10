""" --- Day 8: Seven Segment Search --- """

def get1Words(one, seven):
    list_of_letters = list(one)
    print(list_of_letters)

def getValue(data):
    numbers = {}
    display = {}
    for i in range(10):
        if len(data[i]) == 3:
            numbers[7] = data[i]
        elif len(data[i]) == 2:
            numbers[1] = data[i]
        elif len(data[i]) == 4:
            numbers[4] = data[i]
        elif len(data[i]) == 7:
            numbers[8] = data[i]
    display[1] = get1Words(numbers[1], numbers[7])
    print(numbers)
    return 0

def separateData(data):
    data = data.split()
    separatedList = []
    for i in range(0, len(data), 15):
        separatedList.append([])
        for index in range(i, i+15):
            separatedList[i//15].append(data[index])
    return separatedList

def getSum(data):
    data = separateData(data)
    total = 0
    for el in data:
        total += getValue(el)
    return data

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
    print(getSum(dataInput))
