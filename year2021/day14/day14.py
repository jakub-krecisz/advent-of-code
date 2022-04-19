""" --- Day 14: Extended Polymerization --- """


def getInsertions(dataInput):
    dataInput.pop(0)
    dataInput.pop(0)
    return {a[0] + a[1]: a[6] for a in dataInput}


def getWord(first, second, pairInsertions):
    return pairInsertions[first + second]


def getMostCommon(polymerTemplate):
    words = set(polymerTemplate)
    return max(polymerTemplate.count(word) for word in words)


def getLeastCommon(polymerTemplate):
    words = set(polymerTemplate)
    return min(polymerTemplate.count(word) for word in words)


def getPairs(pairInsertions):
    pairs = {}
    for pair in pairInsertions.keys():
        pairs[pair] = 0
    return pairs


def getPairIntersection(pairs, pairInsertions):
    newPairs = []
    for pair in pairs.keys():
        newPairs.append(pair[0] + pairInsertions[pair])
        newPairs.append(pairInsertions[pair] + pair[1])
    pairs.clear()
    for el in newPairs:
        if el not in pairs:
            pairs[el] = 1
        else:
            pairs[el] += 1

    return pairs


def getSecondResult(dataInput, steps):
    polymerTemplate = dataInput[0]
    pairInsertions = getInsertions(dataInput)
    lastWord = polymerTemplate[-1]
    pairs = {}
    for index in range(1, len(polymerTemplate)):
        pairs[polymerTemplate[index - 1] + polymerTemplate[index]] = 0
    for index in range(1, len(polymerTemplate)):
        pairs[polymerTemplate[index - 1] + polymerTemplate[index]] += 1

    for _ in range(steps):
        pairs = getPairIntersection(pairs, pairInsertions)

    numOfLetters = {}

    for el in pairs.keys():
        if el[0] in numOfLetters:
            numOfLetters[el[0]] += pairs[el]
        else:
            numOfLetters[el[0]] = pairs[el]
    numOfLetters[lastWord] += 1

    return max(numOfLetters.values()) - min(numOfLetters.values())


def getResult(dataIn, steps):
    polymerTemplate = dataIn[0]
    pairInsertions = getInsertions(dataIn)
    intersectedWords = []
    for step in range(steps):
        for index in range(1, len(polymerTemplate)):
            intersectedWords.append(polymerTemplate[index - 1])
            intersectedWords.append(getWord(polymerTemplate[index - 1], polymerTemplate[index], pairInsertions))
        intersectedWords.append(polymerTemplate[len(polymerTemplate) - 1])
        polymerTemplate = intersectedWords
        intersectedWords = []
    mostCommon = getMostCommon(polymerTemplate)
    leastCommon = getLeastCommon(polymerTemplate)
    return mostCommon - leastCommon


if __name__ == '__main__':
    file = 'test_data.txt'
    print(getResult(open(file).read().split('\n'), 10))
    print(getSecondResult(open(file).read().split('\n'), 40))
