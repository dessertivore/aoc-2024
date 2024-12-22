from _common import DIRECTIONS, get_input
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


def get_num_edges(coord:tuple,map:dict) -> tuple[int,set]:
    """
    Check how many coordinates surrounding the current coordinate are the same letter.
    """
    x,y=coord
    count=0
    edges:set=set()
    for direction in DIRECTIONS:
        next=(lambda z,n:(z[0]+n[0],z[1]+n[1]))(direction,coord)
        edge=(lambda z,n:((0.5*z[0])+n[0],(0.5*z[1])+n[1]))(direction,coord)
        if map.get(next) !=map[coord]:
            # if direction[0]!=coord[0]:
            # edges.update({(coord[0]+0.5*direction[0],coord[1]+0.5*direction[1])})
            edges.update({edge})
            # elif direction[1]!=coord[1]:
            #     edges.update({(coord[0]+0.5*direction[0],coord[1]+0.5*direction[1])})
            count+=1
    return count,edges

def count_lines(distinct_edge_coords:set) ->int:
    print(distinct_edge_coords)
    horizontals=set() # i.e. y = 1 or y =2
    verticals=set() # i.e. x = 1 or x=2 as the equation
    for coord in distinct_edge_coords:
        if int(coord[1])!=coord[1]:
            horizontals.update({coord[1]}) 
        if int(coord[0])!=coord[0]:
            verticals.update({coord[0]})
    print(sum([len(verticals),len(horizontals)]))
    # total=0
    # print(horizontals,verticals)
    # for axis in [horizontals,verticals]:
    #     sorted_axis=sorted(axis)
    #     for idx in range(len(axis)-1):
    #         if sorted_axis[idx+1]-sorted_axis[idx]>1:
    #             total+=1
    return sum([len(verticals),len(horizontals)])

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
        total_perim,distinct_edges=get_num_edges(start_coord,coord_to_letter)
        current_visited_area=1
        stack = [start_coord]
        while stack:
            cx, cy = stack.pop()
            for dx, dy in directions:
                neighbour = (cx + dx, cy + dy)
                if neighbour in coord_to_letter and neighbour not in total_visited and coord_to_letter[neighbour] == char:
                    total_visited.add(neighbour)
                    current_visited_perim,current_edges=get_num_edges(neighbour,coord_to_letter)
                    distinct_edges.update(current_edges)
                    total_perim+=current_visited_perim
                    current_visited_area+=1
                    stack.append(neighbour)
        print(char)
        distinct_edges=count_lines(distinct_edges)
        return total_perim,current_visited_area,distinct_edges

    group_count = 0
    for coord, letter in coord_to_letter.items():
        if coord not in total_visited:
            total_visited.add(coord)
            current_visited_perim,current_visited_area,distinct_edges=flood_fill(coord, letter)
            group_areas_and_perims[group_count]=current_visited_area,current_visited_perim,distinct_edges
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
    for area,perim,distinct_edges in flood_fill_dict(test).values():
        total+=(area*perim)
    return total

# assert get_cost(test=True) == 1930
# print(get_cost(test=False))

def part_2(test:bool=False):
    """
    Get the discounted cost of fencing.

    Params:
    -------
    test: bool
        Whether to use test input or not.

    Returns:
    --------
    total_cost: int
        Total cost of the fencing for the elves.
    """
    total_cost=0
    print(flood_fill_dict(test))
    for area,perim,distinct_edges in flood_fill_dict(test).values():
        total_cost+=(area*distinct_edges)
    return total_cost

print(part_2(test=True))
assert part_2(test=True) == 1206