""" --- Day 12: Passage Pathing --- """


def getData(fileName):
    dataIn = []
    for line in open(fileName, 'r').readlines():
        p1, p2 = line.rstrip().split('-')
        dataIn.append((p1, p2))
    return dataIn

def traverse(cave):
    global current_path
    for x in cave:
        if x.islower() and x in current_path:
            continue
        elif x == 'end':
            current_path.append(x)
            path.append(current_path[:])
            current_path.pop()
        else:
            current_path.append(x)
            traverse(M[x])
    current_path.pop()


if __name__ == '__main__':
    dataIn = getData('data.txt')
    M = {}
    path = []

    for row in dataIn:
        if row[0] not in M:
            M[row[0]] = []
        M[row[0]].append(row[1])
        if row[1] not in M:
            M[row[1]] = []
        M[row[1]].append(row[0])
    current_path = ["start"]
    traverse(M["start"])

    print(f'Paths that visit small caves at most once is: {len(path)}')
