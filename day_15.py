from collections import defaultdict
from itertools import count
from _common import get_input

DIRECTION_CHAR_TO_TUPLE:dict={">":(1,0),"<":(-1,0),"^":(0,-1),"v":(0,1)}

def parse_input(test:bool=False, part_2:bool=False) -> tuple[dict,tuple[int,int],str]:
    data=get_input(15,test)
    data=data.split("\n\n")
    raw_map=data[0]
    raw_directions=data[1]
    raw_directions=raw_directions.replace("\n","")
    parsed_map:dict=defaultdict(lambda:None)
    if not part_2:
        for ycoord,line in enumerate(raw_map.split("\n"),0):
            for xcoord,char in enumerate(line,0):
                if char in ["#","O"]:
                    parsed_map[(xcoord,ycoord)]=char
                if char == "@":
                    start=(xcoord,ycoord)
    else:
        for ycoord,line in zip(count(0,2),raw_map.split("\n")):
            for xcoord,char in zip(count(0,2),line):
                if char =="#":
                    for x in range(2):
                        parsed_map[(xcoord+x,ycoord+x)]=char
                elif char == "O":
                    parsed_map[(xcoord,ycoord)]="["
                    parsed_map[(xcoord+1,ycoord)]="]"
                if char == "@":
                    start=(xcoord,ycoord)
    return parsed_map,start,raw_directions

def check_if_box_moves(start:tuple[int, int],direction:str,map:dict, part_2:bool) -> tuple[bool,dict]:
    next = (start[0]+DIRECTION_CHAR_TO_TUPLE[direction][0],start[1]+DIRECTION_CHAR_TO_TUPLE[direction][1])
    if map[next] == "#":
        return False, map
    if not part_2:
        if map[next] is None:
            map[next]="O"
            return True, map
        else:
            return check_if_box_moves(next,direction,map, part_2)
    else:
        if map[next] is None:
            map[start]="["
            map[next]="]"
            return True, map
        else:
            return check_if_box_moves(next,direction,map, part_2)
            



def move(start:tuple[int,int],direction:str, map:dict, part_2:bool=False) -> tuple[tuple[int,int],dict]:
    next = (start[0]+DIRECTION_CHAR_TO_TUPLE[direction][0],start[1]+DIRECTION_CHAR_TO_TUPLE[direction][1])
    if map[next] is None:
        return next, map
    elif map[next] == "#":
        return start, map
    else:
        box_moves,new_map= check_if_box_moves(next,direction,map, part_2)
        if box_moves:
            new_map[next]=None
            return next, new_map
        else:
            return start, map
        
def find_path(test:bool=False) -> int:
    parsed_map,start,raw_directions=parse_input(test)
    
    for direction in raw_directions:
        start,parsed_map=move(start,direction,parsed_map)

    total_gps:int=0
    for coord,char in parsed_map.items():
        if char == "O":
            total_gps+=(100*coord[1])+coord[0]
    return total_gps

assert find_path(test=True) == 10092 
print(find_path(test=False))