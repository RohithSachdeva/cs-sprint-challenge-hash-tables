def has_negatives(a):
    newValues = []
    positiveDict = {}
    singleInts = []
    for i in a:
        if i < 0:
            i = i * -1
            newValues.append(i)
        else: 
            newValues.append(i)
    for x in newValues:
        if x not in positiveDict:
            positiveDict[x] = 1
        else: 
            positiveDict[x] += 1
    for k, v in positiveDict.items():
        if v > 1:
            singleInts.append(k)
    return singleInts

"""

"""

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
