""" --- Day 2: Dive! --- """


def multiply(myList):
    horizontalPos, depth = 0, 0
    for el in myList:
        toListEl = el.split()
        if toListEl[0] == 'forward':
            horizontalPos += int(toListEl[1])
        elif toListEl[0] == 'down':
            depth += int(toListEl[1])
        else:
            depth -= int(toListEl[1])
    return horizontalPos * depth


""" ---- PART ONE ---- """

try:
    myList = []
    while True:
        myList.append(input())
except:
    print(f'The result of multiplying horizontal position by depth is: {multiply(myList)}')
