def has_negatives(a):
    newValues = []
    positiveDict = {}
    singleInts = []
    for i in a: #Create new array of positive values; Look into abs()
        if i < 0:
            i = i * -1
            newValues.append(i)
        else: 
            newValues.append(i)

    for x in newValues: #Count number of instances and cache it 
        if x not in positiveDict:
            positiveDict[x] = 1
        else: 
            positiveDict[x] += 1

    for k, v in positiveDict.items(): #Based on the tests, there were no duplicate positive numbers.. Any v > 1 had a negative counterpart
        if v > 1:
            singleInts.append(k)
    return singleInts

"""
positiveDict = {}
-Check to 
for abs(i) in a:

Solution Ideas-
2 Dictionaries 
Dictionary List Comprehension 

Absolute value variable comparison of two dictionaries 

number_list = [ x for x in a if x  2 == 0]

"""

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
