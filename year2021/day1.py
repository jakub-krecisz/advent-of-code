listOfNumbers = [199,
                 200,
                 208,
                 210,
                 200,
                 207,
                 240,
                 269,
                 260,
                 263]

prefix = [' (N/A - no previous measurement)']

for index in range(1, len(listOfNumbers)):
    if listOfNumbers[index - 1] > listOfNumbers[index]:
        prefix.append(' (Decreased)')
    else:
        prefix.append(' (Increased)')

for num in range(len(listOfNumbers)):
    listOfNumbers[num] = str(listOfNumbers[num]) + prefix[num]

for el in listOfNumbers:
    print(el)
