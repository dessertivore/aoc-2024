from _common import get_input


def parse_input(test:bool=False) -> tuple[dict,tuple]:
    """
    Parse the input into a dictionary of coordinates of obstacles, and find start point
    of guard.

    Params:
    -------
    test: bool
        Whether to use the test input.

    Returns:
    --------
    lab_map: dict
        Dictionary of coordinates of obstacles.

    start: tuple
        Starting point of guard.
    """
    lab_map={}
    for ycoord,line in enumerate(get_input(6,test).split("\n"),0):
        for xcoord,letter in enumerate(line,0):
            lab_map[(xcoord,ycoord)]=letter
            if letter=="^":
                start=(xcoord,ycoord)
    return lab_map,start

def find_repeated_subarrays(lst:list):
    """
    Efficiently check if there are repeated subarrays in the list.
    """
    seen = set()
    for length in range(4, len(lst) + 1):  # Only check subarrays of length >= 4
        window_hash = hash(tuple(lst[:length]))  # Compute initial hash
        seen.add(window_hash)

        for i in range(1, len(lst) - length + 1):
            window_hash = hash(tuple(lst[i:i + length]))  # Hash sliding window
            if window_hash in seen:
                return True
            seen.add(window_hash)

    return False


def move_guard(test:bool=False, part_2_map:dict|None=None) -> tuple[int,list]:
    """
    Find how many distinct positions will the guard visit before leaving the mapped 
    area.

    Params:
    -------
    test: bool
        Whether to use the test input.

    Returns:
    --------
    counter: int
        Number of distinct positions visited by the guard.

    route: list
        Set of all positions visited by the guard.
    """
    lab_map,next=parse_input(test)
    if part_2_map:
        lab_map=part_2_map
    route: list=[]
    direction=(0,-1)
    counter=0
    
    TURN={(0,1):(-1,0),(1,0):(0,1),(0,-1):(1,0),(-1,0):(0,-1)}

    while next:
        if next not in lab_map:
            break

        if part_2_map and (next in route):
            if find_repeated_subarrays(route):
                raise ValueError("REPEATED")
        
        if lab_map[next] != "#":
            # At obstacles, guard will turn    
            if lab_map[next]:
                counter+=1
            # lab_map[next]=False
            next=(next[0]+direction[0],next[1]+direction[1])
            
            
        else:
            # Reverse, then turn correct way
            next=(next[0]-direction[0],next[1]-direction[1])
            direction=TURN[direction]
            next=(next[0]+direction[0],next[1]+direction[1])
        route.append(next)
        

        
    return counter,route

assert move_guard(test=True)[0]==41
# print(move_guard()[0])

def add_obstruction(test:bool=False):
    """
    Start on part 2. Currently works on test but is not efficient enough for full data.
    """
    lab_map,_=parse_input(test)
    route=move_guard(test)[1]
    counter=set()
    for coord in set(route):
        if lab_map.get(coord)!="#":
            lab_map[coord]="#"
            try:
                move_guard(test,lab_map)
            except Exception:
                counter.add(coord)
            finally:
                lab_map[coord]=False
    return len(counter)

assert add_obstruction(test=True)==6
print(add_obstruction(test=False))