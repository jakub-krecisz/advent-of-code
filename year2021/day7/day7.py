""" --- Day 7: The Treachery of Whales --- """


def getKey(leasFuel, dictionary):
    for key, value in dictionary.items():
        if leasFuel == value:
            return key


def getPosAndFuel(data):
    maxPosition, minPosition = max(data), min(data)
    positions = {}
    for pos in range(minPosition, maxPosition + 1):
        fuel = 0
        for crab in data:
            fuel += abs(pos - crab)
        positions[pos] = fuel
    leastFuel = min(positions.values())
    bestPosition = getKey(leastFuel, positions)

    return f'Best position is: {bestPosition}, this position need {leastFuel} fuel'


if __name__ == '__main__':
    dataFile = open('data.txt')
    dataInput = dataFile.read().split(',')
    toInt = map(int, dataInput)
    intDataInput = list(toInt)

    print(getPosAndFuel(intDataInput))
