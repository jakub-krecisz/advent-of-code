""" --- Day 6: Lantern fish --- """


def toInt(list):
    for index in range(len(list)):
        list[index] = int(list[index])
    return list


def getNumOfFish(fishes, days):
    fishes = toInt(fishes)
    fishCollection = {}

    for i in range(9):
        fishCollection[i] = 0

    for fish in fishes:
        fishCollection[fish] += 1

    for day in range(days):
        """ Uncomment if you want to see every day values """
        # print(f'Day {day}', end=' ')
        # print(fishCollection.values())
        previousDay = fishCollection[0]
        for key in fishCollection.keys():
            if key != 8:
                fishCollection[key] = fishCollection[key + 1]
        fishCollection[8] = previousDay
        fishCollection[6] += previousDay

    return sum(fishCollection.values())


if __name__ == '__main__':
    dataFile = open('data.txt')
    dataInput = dataFile.read().split(',')
    print(f'Result: {getNumOfFish(dataInput, 256)}')
