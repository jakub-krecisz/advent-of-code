""" ---- PART ONE ---- """


def measurement(listOfNumbers):
    countOfIncrease = 0
    for index in range(1, len(listOfNumbers)):
        if listOfNumbers[index - 1] < listOfNumbers[index]:
            countOfIncrease += 1
    return countOfIncrease


try:
    myList = []
    while True:
        myList.append(int(input()))
except:
    print(f'Measurements which are larger than the previous one: {measurement(myList)}')
