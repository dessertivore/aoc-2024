from collections import defaultdict
from _common import get_input, DIRECTIONS

def parse_input(test:bool=False, time:int|None=None)->dict:
    data=get_input(18,test)
    coords_map:dict=defaultdict(lambda:None)
    if time:
        counter=time
    for line in data.splitlines():
        coords=tuple([int(x) for x in line.split(",")])
        coords_map[coords]="#"
        if time:
            counter-=1
            if counter ==0:
                break
    return coords_map

MEMO_MAP:dict=defaultdict(lambda:None)

def go_next(start:tuple,direction:tuple,maxx:int,maxy:int,map:dict,visited:set)->int|float:
    next=(start[0]+direction[0],start[1]+direction[1])
    if any([(next in visited), (map[next] is not None), (next[0] not in range(maxx+1)),(next[1] not in range(maxy+1))]):
        return float('inf')
    elif next[0]==maxx and next[1]==maxy:
        return 1
    else:
        visited.add(next)
        return 1 + min ([go_next(next,dir,maxx,maxy,map,visited) for dir in DIRECTIONS])
    
def navigate_map(test:bool=False,time:int|None=None):
    map = parse_input(test,time)
    if test:
        maxx=6
        maxy=6
    else:
        maxx=70
        maxy=70
    size=maxx*maxy
    start=(0,0)
    visited:set={start}
    return min([go_next(start,dir,maxx,maxy,map, visited) for dir in DIRECTIONS])

assert navigate_map(test=True,time=12)==24
# print(navigate_map(test=False,time=1024))

    
