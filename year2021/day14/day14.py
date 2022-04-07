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
    dataIn = open('data.txt').read().split('\n')
    print(getResult(dataIn, 10))
