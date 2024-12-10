from collections import defaultdict
from _common import get_input


def parse_map(test:bool=False) -> tuple[dict,set]:
    """
    Parse topographical map information into a dictionary of coordinates and their 
    values, and a set of starting points (0s).

    Params:
    -------
    test: bool
        Whether to use test data or not.

    Returns:
    --------
    tuple[dict,set]
        Dictionary of coordinates and their values, and a set of starting points.
    
    """
    coorddict=defaultdict(lambda:-1)
    start_points=set()
    for ycoord,line in enumerate(get_input(10,test).split("\n")):
        for xcoord,char in enumerate(line,0):
            coorddict[xcoord,ycoord]=int(char)
            if char=="0":
                start_points.add((xcoord,ycoord))
    return coorddict,start_points


DIRECTIONS=[(1,0),(-1,0),(0,1),(0,-1)]

def start_trail(test:bool=False,find_score:bool=True) -> int:
    """
    Parse input and find the number of trails that start at 0 and end at 9, in 
    increments of 1.

    Params:
    -------
    test: bool
        Whether to use test data or not.
    
    find_score: bool
        Whether to find the score or not. If not finding score, it will find the rating
        instead.

    Returns:
    --------
    int
        Either score, or rating of trails on map, depending on what has been set.
    """
    coorddict,start_points=parse_map(test)
    counter=0
    for start_point in start_points:
        visited:set=set()
        for direction in DIRECTIONS:
            counter+=follow_trails(coorddict,start_point,next=(lambda x,y: (x[0]+y[0],x[1]+y[1]))(start_point,direction),visited=visited,find_score=find_score)
    return counter
            
def follow_trails(coorddict:dict,start_point:tuple, next:tuple, visited:set,find_score:bool) -> int:
    """
    Follow trails started in start_trail function. Recursively checks the various 
    possible directions of travel for each trail.

    Params:
    -------
    coorddict: dict
        Dictionary of coordinates and their values.

    start_point: tuple
        The starting point which we are checking from.

    next: tuple
        The next point to check.
    
    visited: set
        The set of visited points.

    find_score: bool
        Whether to find the score or not. If not finding score, it will find the rating
        instead.

    Returns:
    --------
    int
        Either score, or rating of trails from the start point provided, depending on
        what has been set.
    
    """
    if next in visited:
        return 0
    if coorddict[next] == coorddict[start_point]+1:
        if find_score:
            visited.add(next)
        if coorddict[next] == 9:
            return 1
        
        else:
            counter=0
            for direction in DIRECTIONS:
                next_step=(lambda x,y: (x[0]+y[0],x[1]+y[1]))(next,direction)
                counter+= follow_trails(coorddict,start_point=next,next=next_step,visited=visited,find_score=find_score)
            return counter  
    return 0

assert start_trail(test=True) == 36
assert start_trail(test=True, find_score=False) == 81

print(start_trail(False, find_score=False))

