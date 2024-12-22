from _common import get_input
from collections import defaultdict

def parse_input(test: bool=False) -> dict:
    """
    Parse input for day 12.
    """
    lines = get_input(12,test).split("\n")
    coord_to_letter:dict=defaultdict(lambda:[])
    for ycoord,line in enumerate(lines,0):
       for xcoord, letter in enumerate(line,0):
        coord_to_letter[(xcoord,ycoord)]=letter
    return coord_to_letter


def get_num_edges(coord:tuple,map:dict) -> int:
    """
    Check how many coordinates surrounding the current coordinate are the same letter.
    """
    x,y=coord
    count=0
    if map.get((x+1,y)) !=map[coord]:
        count+=1
    if map.get((x-1,y)) !=map[coord]:
        count+=1
    if map.get((x,y+1)) !=map[coord]:
        count+=1
    if map.get((x,y-1)) !=map[coord]:
        count+=1
    return count

def flood_fill_dict(test:bool=False):
    """
    Use flood fill to find the area and perimeter of each group of letters.

    Params:
    -------
    test: bool
        Whether to use test input or not.

    Returns:
    --------
    group_areas_and_perims: dict
        Dictionary containing the area and perimeter of each group of letters
    """
    coord_to_letter= parse_input(test)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    group_areas_and_perims:dict=defaultdict(lambda:0)
    total_visited:set=set()
    
    def flood_fill(start_coord, char):
        current_visited_perim=get_num_edges(start_coord,coord_to_letter)
        current_visited_area=1
        stack = [start_coord]
        while stack:
            cx, cy = stack.pop()
            for dx, dy in directions:
                neighbor = (cx + dx, cy + dy)
                if neighbor in coord_to_letter and neighbor not in total_visited and coord_to_letter[neighbor] == char:
                    total_visited.add(neighbor)
                    current_visited_perim+=get_num_edges(neighbor,coord_to_letter)
                    current_visited_area+=1
                    stack.append(neighbor)
        return current_visited_perim,current_visited_area

    group_count = 0
    for coord, letter in coord_to_letter.items():
        if coord not in total_visited:
            total_visited.add(coord)
            current_visited_perim,current_visited_area=flood_fill(coord, letter)
            group_areas_and_perims[group_count]=current_visited_area,current_visited_perim
            group_count += 1

    return group_areas_and_perims

def get_cost(test:bool=False):
    """
    Get the total cost of the fencing for the elves.

    Params:
    -------
    test: bool
        Whether to use test input or not.

    Returns:
    --------
    total: int
        Total cost of the fencing for the elves.
    """
    total=0
    for area,perim in flood_fill_dict(test).values():
        total+=(area*perim)
    return total
    
assert get_cost(test=True) == 1930
print(get_cost(test=False))