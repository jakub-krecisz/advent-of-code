
def correctList(list):
    correctedList = []
    for el in list:
        coords = el[:el.find(' -> ')].split(',') + el[el.find(' -> ')+4:].split(',')
        correctedList.append(coords)
    return correctedList

def getCross(list):
    x, y = 0, 0
    for el in list:
        if x < max(int(el[0]), int(el[2])):
            x = max(int(el[0]), int(el[2]))
        if y < max(int(el[1]), int(el[3])):
            y = max(int(el[1]), int(el[3]))
    cross = [[0 for _ in range(x)] for _ in range(y)]
    return cross


def getNumOfPoints(myList):
    myList = correctList(myList)
    cross = getCross(myList)
    cross = fillCross(cross, myList)









if __name__ == '__main__':
    try:
        myList = []
        while True:
            myList.append(input())
    except:
        print(getNumOfPoints(myList))