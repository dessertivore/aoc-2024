import copy
from _common import get_input

def parse_input(test:bool=False):
    data=get_input(2,test)
    output:list=[]
    for line in data.split("\n"):
        if not line:
            continue
        output.append([int(x) for x in line.split(" ")])
    return output


def all_inc_or_dec(data: list, reverse: bool=False):
    """
    For a list of ints, check if all are increasing or if all are decreasing.
    To check for decreasing, set reverse to True, as this reverses the sort order.

    Returns false if neither condition is met.

    """
    sorted = copy.deepcopy(data)
    sorted.sort(reverse=reverse)
    return sorted == data

def check_safe(test:bool=False, try_remove_one:bool=False) -> dict[int, bool]:
    """
    Check if a level is defined as safe.
    First, check if all numbers are increasing or decreasing.
    Then, check if the difference between each number is 1-3.
    Return a dict stating if each level is safe (True) or not (False).

    Params:
    -------
    test: bool
        If True, use test data.

    Returns:
    --------
    dict[int, bool]
        A dictionary with the level number as the key and a boolean (whether safe or 
        not) as the value.
    """
    data=parse_input(test)
    output:dict={}
    for enum, line in enumerate(data):
        # Check if all numbers are increasing or decreasing.
        output[enum]=any([all_inc_or_dec(line), all_inc_or_dec(line, reverse=True)])
        if try_remove_one:
            for x in range(len(line)-1):
                copy_line=copy.deepcopy(line)
                copy_line.pop(x)
                if any([all_inc_or_dec(copy_line), all_inc_or_dec(copy_line, reverse=True)]):
                    output[enum]=True
                    break
        prev=None
        if try_remove_one:
            # Allow tolerance of 1 bad level.
            mistakes_so_far=0
        for x in line:
            # Check there is a difference of 1-3 between each number.
            if not prev:
                prev=x
                continue
            if abs(x - prev) not in range(1,4):
                if try_remove_one:
                    if mistakes_so_far==0:
                        mistakes_so_far+=1
                        continue
                output[enum]=False
                break
            prev=x
    return output

def count_safe(test:bool=False, try_remove_one:bool=False) -> int:
    return sum(check_safe(test, try_remove_one).values())

assert check_safe(test=True)=={0: True, 1: False, 2: False, 3: False, 4: False, 5: True}
assert count_safe(test=True)==2
assert check_safe(test=True,try_remove_one=True)=={0: True, 1: False, 2: False, 3: True, 4: True, 5: True}
assert count_safe(test=True,try_remove_one=True)==4

print(count_safe(try_remove_one=True))