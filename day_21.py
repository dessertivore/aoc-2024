import re
from _common import DIRECTIONS, get_input
from collections import deque

def parse_input(test:bool=False) -> list:
    sequences=[]
    for line in get_input(21,test).splitlines():
        sequences.append(line)
    return sequences

def get_nums(test:bool=False)->list:
    all_nums=[]
    for line in get_input(21,test).splitlines():
        nums=re.findall('[0-9]+',line)
        all_nums.append(int(nums[0]))
    return all_nums

assert get_nums(test=True) == [29, 980, 179, 456, 379]

GRID = {
    '1': (0, 2), '2': (1,2), '3': (2,2),
    '4': (0, 1), '5': (1, 1), '6': (2, 1),
    '7': (0, 0), '8': (1, 0), '9': (2, 0),
    '0': (1, 3), 'A': (2, 3)
}
SECONDARY_GRID:dict={"^":(1,0),">":(2,1),"v":(1,1),"A":(2,0),"<":(0,1),}

DIR_TO_SYMBOL:dict={(1,0):">",(0,-1):"^",(0,1):"v",(-1,0):"<"}
KNOWN_ROUTES:dict={}

def shortest_path_between_chars(start: str, end: str, grid:dict=GRID):
    """
    Find shortest path between characters and return the route taken, not just 
    the number of steps.
    """
    # if route:=KNOWN_ROUTES.get((start,end)):
    #     return route
    start_pos=grid[start]
    end_pos=grid[end]
    visited=set()
    queue=deque([(start_pos,0,[])])
    while queue:
        pos, steps, directions_taken=queue.popleft()
        if pos==end_pos:
            KNOWN_ROUTES[start,end]=steps, directions_taken
            return steps, directions_taken
        if pos in visited:
            continue
        visited.add(pos)
        for direction in DIR_TO_SYMBOL.keys():
            new_pos=(pos[0]+direction[0],pos[1]+direction[1])
            if new_pos in grid.values():
                queue.append((new_pos,steps+1,directions_taken+[direction]))
    return None


def length_of_path(test:bool=False):
    all_lens=0
    all_directions=[]
    for line in parse_input(test):
        this_line=[]
        # insert A between every character
        total_len=0
        line="A"+line
        for idx in range(len(line)-1):
            steps,directions_taken=shortest_path_between_chars(line[idx],line[idx+1])
            this_line.extend([DIR_TO_SYMBOL[x] for x in directions_taken])
            this_line.extend("A")
            total_len+=steps
        all_lens+=total_len
        all_directions.append(this_line)
    return all_directions

assert length_of_path(test=True)[0]==[x for x in "<A^A>^^AvvvA"]


def first_layer_abstraction(test:bool=False,first_layer:bool=True,second_layer_directions:list|None=None):
    all_lens=0
    all_directions=[]
    if first_layer:
        lines=length_of_path(test)
    else:
        lines=second_layer_directions
    for line in lines:
        this_line=[]
        # insert A between every character
        total_len=0
        line=["A"]+line
        for idx in range(len(line)-1):
            steps,directions_taken=shortest_path_between_chars(line[idx],line[idx+1],grid=SECONDARY_GRID)
            this_line.extend([DIR_TO_SYMBOL[x] for x in directions_taken])
            this_line.extend("A")
            total_len+=steps
        all_lens+=total_len
        all_directions.append(this_line)
    return all_directions

def second_layer(test:bool=False):
    all_directions=first_layer_abstraction(test)
    secondary=first_layer_abstraction(test,first_layer=False,second_layer_directions=all_directions)
    return secondary


assert len(first_layer_abstraction(test=True)[0])==len([x for x in "v<<A>>^A<A>AvA<^AA>A<vAAA>^A"])
assert len(second_layer(test=True)[0])==len("""<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A""")
assert len(second_layer(test=True)[1])==len("""<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A""")
assert len(second_layer(test=True)[2])==len("""<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A""")
assert len(second_layer(test=True)[3])==len("""<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A""")
print(length_of_path(test=True)[4])
print(first_layer_abstraction(test=True)[4])
print(second_layer(test=True)[4],len("""<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"""))
assert len(second_layer(test=True)[4])==len("""<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A""") # This test is failing :( )

def calculate_complexity(test:bool=False):
    total=0
    directions=second_layer(test)
    nums=get_nums(test)
    for idx in range(len(nums)):
        total+=nums[idx]*len(directions[idx])
    return total

assert calculate_complexity(test=True)==126384
print(calculate_complexity(test=False))