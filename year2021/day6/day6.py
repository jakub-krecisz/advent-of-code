""" --- Day 6: Lantern fish --- """


def toInt(list):
    for index in range(len(list)):
        list[index] = int(list[index])
    return list


def getNumOfFish(fishes, days):
    fishes = toInt(fishes)

    for i in range(days):
        for listIndex in range(len(fishes)):
            if fishes[listIndex] > 0:
                fishes[listIndex] -= 1
            else:
                fishes[listIndex] = 6
                fishes.append(8)

    return len(fishes)


if __name__ == '__main__':
    dataFile = open('data.txt')
    myList = dataFile.read().split(',')
    print(getNumOfFish(myList, 80))
