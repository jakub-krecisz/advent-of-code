""" --- Day 9: Smoke Basin --- """


def getCross(listInput):
    for index in range(len(listInput)):
        listInput[index] = list(listInput[index])
        listInput[index] = [int(x) for x in listInput[index]]
        listInput[index].insert(0, 9)
        listInput[index].insert(len(listInput[index]), 9)
    listInput.insert(0, [9 for _ in range(len(listInput[0]))])
    listInput.insert(len(listInput), [9 for _ in range(len(listInput[0]))])
    return listInput


def getSumOfTheRisk(dataIn):
    dataCross = getCross(dataIn)
    heights = []

    for rowIndex in range(1, len(dataCross) - 1):
        for colIndex in range(1, len(dataCross[rowIndex]) - 1):
            if dataCross[rowIndex][colIndex] < min(dataCross[rowIndex - 1][colIndex],
                                                   dataCross[rowIndex + 1][colIndex],
                                                   dataCross[rowIndex][colIndex - 1],
                                                   dataCross[rowIndex][colIndex + 1], ):
                heights.append(dataCross[rowIndex][colIndex])
    return sum(heights) + len(heights)


def check_neighbors(data, basin_points, more_neighbors):
    all_neighbors = {}
    for i, j in more_neighbors.keys():
        new_neighbors = {x: int(data[x[0]][x[1]]) for x in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)] if
                         -1 not in x and 100 not in x and x not in basin_points.keys() and int(data[x[0]][x[1]]) != 9}
        all_neighbors = {**all_neighbors, **new_neighbors}
    return all_neighbors


def get_basins(data):
    basins_list = []
    for i in range(len(data)):
        for j in range(len(data)):
            starting_value = int(data[i][j])
            if (i, j) not in [basins_list[i][j][0] for i in range(len(basins_list)) for j in
                              range(len(basins_list[i]))] and starting_value != 9:
                neighbors = {x: int(data[x[0]][x[1]]) for x in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)] if
                             -1 not in x and 100 not in x and int(data[x[0]][x[1]]) != 9}
                basin_points = {**{(i, j): starting_value}, **neighbors}
                more_neighbors = check_neighbors(data, basin_points, neighbors)
                basin_points = {**basin_points, **more_neighbors}
                while more_neighbors != {}:
                    more_neighbors = check_neighbors(data, basin_points, more_neighbors)
                    basin_points = {**basin_points, **more_neighbors}
                basins_list.append(sorted(basin_points.items()))
            else:
                continue
    return sorted([len(x) for x in basins_list])[-1] * sorted([len(x) for x in basins_list])[-2] * \
           sorted([len(x) for x in basins_list])[-3]


if __name__ == "__main__":
    dataFile = open('data.txt')
    dataInput = dataFile.read().split()
    print(f'Sum of the risk levels of all low points: {getSumOfTheRisk(dataInput)}')
    print(f"Product of three lagerst basins: {get_basins(dataInput)}")
