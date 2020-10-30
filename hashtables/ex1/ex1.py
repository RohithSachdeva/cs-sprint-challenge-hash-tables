import sys
def get_indices_of_item_weights(weights, length, limit):
    weightDictionary = {}

    for i in range(length): #Append keys as weight index = to position in length array
        weightDictionary[weights[i]] = i
    
    
    for i in range(len(weights)): #Iterate through the weights
        desiredValue = limit - weights[i] #Value we would want 
        if desiredValue in weightDictionary: #If that value is found
            if i > weightDictionary[desiredValue]: #Compare index locations
                return (i, weightDictionary[desiredValue])
            else:
                return (weightDictionary[desiredValue], i)
            
            #if the key 

            #How to print the position of current i in weights with weightDictionary key we found?  Also need to have bigger value first 

            # i is the position of the array we're interested in.. 

            #Missing the logic for 7 - 0 ... 
            #Limit is 7 ... so our desired value is 
    

    """
    for i in weightDictionary:
        desiredValue = limit - weightDictionary[i] <-- this would compare limit - index position ... not what we want 
        if desiredValue in weightDictionary:
            return (weightDictionary)
    """
    
    
  


    #limit - weight 



    

    
    

    
    



    


"""
1. Iterate through weights list.  Create dictionary with weights as Keys and their index as value 

What can I use to have (limit - weight) = another weight within the weights array?  
  
I want the key to be what I'm searching for and the value to be what I'm interested in. 

x = limit - (values in the weights array);  If x is found in the weight dictionary, 

How does a hash table help make this faster? 
Though there are two nested loops, searching through a hash table speeds up the process heavily.  

2. 
"""