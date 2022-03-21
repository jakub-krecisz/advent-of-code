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


def secondTraverse(cave):
    global current_path
    global second_small
    for x in cave:
        if x.islower() and x in current_path:
            if not second_small[0] and x != "start" and x != "end":
                second_small = (True, x)
                current_path.append(x)
                secondTraverse(M[x])
            continue
        elif x == 'end':
            current_path.append(x)
            path.append(current_path[:])
            current_path.pop()
        else:
            current_path.append(x)
            secondTraverse(M[x])
    if current_path.pop() == second_small[1]:
        second_small = (False, "")


if __name__ == '__main__':
    # Part one
    M, path = {}, []
    for row in getData('data.txt'):
        if row[0] not in M:
            M[row[0]] = []
        M[row[0]].append(row[1])
        if row[1] not in M:
            M[row[1]] = []
        M[row[1]].append(row[0])

    current_path = ["start"]
    second_small = (False, "")
    traverse(M["start"])

    print(f'Paths that visit small caves at most once is: {len(path)}')

    # Part Two
    M, path = {}, []
    for a in getData('data.txt'):
        if a[0] not in M:
            M[a[0]] = []
        M[a[0]].append(a[1])
        if a[1] not in M:
            M[a[1]] = []
        M[a[1]].append(a[0])

    current_path = ["start"]
    second_small = (False, "")
    secondTraverse(M["start"])

    print(f'Paths through this cave system is: {len(path)}')
