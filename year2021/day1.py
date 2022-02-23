""" ---- PART ONE ---- """


def measurement(listOfNumbers):
    countOfIncrease = 0
    for index in range(1, len(listOfNumbers)):
        if listOfNumbers[index - 1] < listOfNumbers[index]:
            countOfIncrease += 1
    return countOfIncrease

def secondMeasurement(listOfNumbers):
    countOfIncrease = 0
    for index in range(1, len(listOfNumbers) - 2):
        if (listOfNumbers[index - 1] + listOfNumbers[index] + listOfNumbers[index + 1]) <\
                (listOfNumbers[index] + listOfNumbers[index + 1] + listOfNumbers[index + 2]):
            countOfIncrease += 1
    return countOfIncrease

try:
    myList = []
    while True:
        myList.append(int(input()))
except:
    print(f'Measurements which are larger than the previous one: {measurement(myList)}')


""" ---- PART TWO ---- """

print(f'Three measurements which are larger than the three previous measurements: {secondMeasurement(myList)}')

