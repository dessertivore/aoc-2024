from _common import get_input

def parse_input(test: bool=False) -> list:
    """
    Parse input for day 11. 

    Params:
    -------
    test: bool
        Whether to use test data or not.

    Returns:
    --------
    list
        List of rocks.
    """
    rocks = get_input(11,test).strip("\n")
    return rocks.split(" ")

discovered:dict={}

def manage_even_length(rock:str) -> list:
    """
    Evolution of rocks with a number of even length engraved on them.

    Params:
    -------
    rock: str
       Number of even length engraved on it.

    Returns:
    --------
    list
        List of numbers that the rock evolves into.
    """
    unprocessed_nums=[rock[:int(len(rock)/2)],rock[int(len(rock)/2):]]
    new_nums:list=[]
    for num in unprocessed_nums:
        num=num.lstrip("0")
        if num == "":
            num="0"
        new_nums.append(num)
    return new_nums

def evolve_rocks(rocks_dict: dict) -> dict:
    """
    Blink once. This causes the rocks to evolve. They are processed within a dict, as 
    the order does not matter.

    Params:
    -------
    rocks: dict
        Dict of rocks:number of rocks with that number. 

    Returns:
    --------
    dict
        Mapping engraved number:number of rocks with that number.
    """
    new_rocks:dict={}

    for rock,num_rocks in rocks_dict.items():
        if rock in discovered:
            if isinstance(discovered[rock],str): 
                new_rocks[discovered[rock]] = new_rocks.get(discovered[rock], 0) + num_rocks
            else:
                for y in discovered[rock]:
                    new_rocks[y] = new_rocks.get(y, 0) + num_rocks
        elif rock == "0":
            discovered[rock]="1"
            new_rocks["1"] = new_rocks.get("0", 0) + num_rocks
        elif len(rock)%2 == 0:
            discovered[rock]=manage_even_length(rock)
            for y in discovered[rock]:
                    new_rocks[y] = new_rocks.get(y, 0) + num_rocks
        else:
            discovered[rock]=str(int(rock)*2024)
            new_rocks[discovered[rock]] = new_rocks.get(discovered[rock], 0) + num_rocks
    return new_rocks


def blink_x_times(test:bool=False,blinks:int=1) -> int:
    """
    Processes list of rocks into a dict, mapping each engraved number to the number of
    rocks it is found on.
    Evolve the rocks a specified number of times.

    Params:
    -------
    test: bool
        Whether to use test data or not.

    blinks: int
        Number of times to evolve the rocks.

    Returns:
    --------
    int
        Number of rocks after evolving the rocks a specified number of times.
    """
    rocks_list:list=parse_input(test)
    rocks_dict:dict={}
    for rock in rocks_list:
        rocks_dict[rock]=rocks_dict.get(rock,0)+1
    for x in range(blinks):
        new=evolve_rocks(rocks_dict)
        rocks_dict=new
    return sum(rocks_dict.values())

assert list(evolve_rocks({"125":1,"17":1}))==["253000", "1","7"]
assert blink_x_times(test=True, blinks=6)==22
assert blink_x_times(test=True, blinks=25)==55312
print(blink_x_times(test=False, blinks=75))