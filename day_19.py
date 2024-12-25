from _common import get_input

def parse_input(test:bool=False):
    raw=get_input(19,test).split("\n\n")
    towels=set(raw[0].split(", "))
    desired_designs=raw[1].splitlines()
    return towels,desired_designs

def parse_towels_to_pattern(pattern:str,towel:str,towels:list,cache:dict,pattern_obtained_so_far:str=""):
    key = pattern_obtained_so_far + towel
    if key in cache:
        return cache[key]
    if key == pattern:
        cache[key] = 1
        return 1
    elif len(key) >= len(pattern) or key != pattern[:len(key)]:
        cache[key] = 0
        return 0
    cache[key] = sum(parse_towels_to_pattern(pattern, next_towel, towels, pattern_obtained_so_far=key, cache=cache) for next_towel in towels if len(pattern_obtained_so_far+next_towel)<=len(pattern))
    return cache[key]

def parse_all_patterns(test:bool=False,part_2:bool=False):
    towels,desired_designs=parse_input(test)
    counter=0
    for pattern in desired_designs:
        cache:dict={}
        if (curr_sum:=sum([parse_towels_to_pattern(pattern,towel,towels,cache=cache) for towel in towels])) >= 1:
            if not part_2:
                counter+=1
            else:
                counter+=curr_sum
    return counter


assert parse_all_patterns(test=True) == 6
assert parse_all_patterns(test=True,part_2=True)==16
print(parse_all_patterns(part_2=True))
