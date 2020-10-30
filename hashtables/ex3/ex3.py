def intersection(arrays):
    cache = {}
    result = []

    arrayLength = len(arrays)

    for i in arrays: #iterate through array
        for k in i: #Increment repeated values  
            if k in cache:
                cache[k] += 1
            else:
                cache[k] = 1
            if cache[k] == arrayLength: #If the count == arrayLength, they appeared in all of the arrays
                result.append(k)
                
    return result

"""

"""

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
