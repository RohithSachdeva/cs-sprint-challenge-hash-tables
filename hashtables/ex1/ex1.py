import sys
def get_indices_of_item_weights(weights, length, limit):
    weightDictionary = {}
    count = 0
    for x in weights:
        weightDictionary[x] = count
        count += 1

    for (k, v) in weightDictionary.items():
        if (limit - v) in weightDictionary:
             
            answer = [weightDictionary[g], weightDictionary[h]]
        elif g + g == limit:
            answer = [weightDictionary[g], weightDictionary[g]]
    return answer
    """



    


"""
1. Iterate through weights list.  Keep a counter to store their value as their position in the array.  Store its weight as the key and position as the value

2. For k, v in dictionary.. if k less than limit.. we can create another dictionar y 
"""