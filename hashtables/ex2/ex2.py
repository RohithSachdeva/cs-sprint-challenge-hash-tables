import sys
#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    travel = {}
    route = [None] * length

    for x in tickets:
        travel[x.source] = x.destination

    route[0] = travel["NONE"]
    print(travel)
    sys.exit()
    
    

    return route


"""
Output = ["LAX", "SFO" etc...] 
Tickets is an array of class objects?  
Where ticket.source = key and ticket.destination = value
If source or destination = "NONE" .. starting or ending point 

"""