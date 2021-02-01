def intersection(arrays):
    cache = {}
    result = []
    
    array_length = len(arrays)

    for i in arrays:
        for k in i:
            if k in cache:
                cache[k] += 1
            else: 
                cache[k] = 1
            if cache[k] == array_length:
                result.append(k)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))


"""
Given multiple lists.. Find the numbers that exist concurrently across those 3 lists

So for i in array... for k in i sort of loop ... cache numbers that exist concurrently 

If you find k of i (the iteration) append the result to the result array 
"""