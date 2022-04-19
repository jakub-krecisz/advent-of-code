""" --- Day 15: Chiton --- """

def getTheLowestRisk(dataIn):
    coords = [[0, 0]]
    for step in range(len(dataIn) + len(dataIn[0])):
        if coords[step][0] + 1 < coords[step][1] + 1:
            coords.append()


if __name__ == '__main__':
    file = 'test_data.txt'
    print(getTheLowestRisk(open(file).read().split()))
