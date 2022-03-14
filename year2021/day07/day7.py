""" --- Day 7: The Treachery of Whales --- """


def getKey(leasFuel, dictionary):
    for key, value in dictionary.items():
        if leasFuel == value:
            return key

def getFuel(distance):
    fuel = 0
    for i in range(distance + 1):
        fuel += i
    return fuel

def getPosAndFuel(data):
    maxPosition, minPosition = max(data), min(data)
    positions = {}
    for pos in range(minPosition, maxPosition + 1):
        print(f'Checking {pos} position of {abs(minPosition - maxPosition)} positions')
        fuel = 0
        for crab in data:
            fuel += getFuel(abs(pos - crab))
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
