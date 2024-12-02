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

def check_report_safe(report: list)->bool:
    # Check if all numbers are increasing or decreasing.
    safe=any([all_inc_or_dec(report), all_inc_or_dec(report, reverse=True)])
    if not safe:
        return safe
    
    prev=None
    for x in report:
        # Check there is a difference of 1-3 between each number.
        if not prev:
            prev=x
            continue
        if abs(x - prev) not in range(1,4):
            safe=False
            break
        prev=x
    return safe  
      
def check_all_safe(test:bool=False, try_remove_one:bool=False) -> dict[int, bool]:
    """
    Check if a level is defined as safe.
    First, check if all numbers are increasing or decreasing.
    Then, check if the difference between each number is 1-3.
    Return a dict stating if each level is safe (True) or not (False).

    Params:
    -------
    test: bool
        If True, use test data.
    try_remove_one: bool
        If True, try to remove one number at a time to see if possible to make the 
        level safe with the Problem Dampener.

    Returns:
    --------
    dict[int, bool]
        A dictionary with the level number as the key and a boolean (whether safe or 
        not) as the value.
    """
    data=parse_input(test)
    output:dict={}
    for enum, line in enumerate(data):
        if check_report_safe(line):
            output[enum]=True
        else:
            output[enum]=False
        
        if not output[enum] and try_remove_one:
            for x in range(len(line)):
                copy_line=copy.deepcopy(line)
                copy_line.pop(x)
                if check_report_safe(copy_line):
                    output[enum]=True
                    break
    return output

def count_safe(test:bool=False, try_remove_one:bool=False) -> int:
    """
    Count how many total reports are safe.

    Params:
    -------
    test: bool
        If True, use test data.
    try_remove_one: bool
        If True, try to remove one number at a time to see if possible to make the 
        level safe with the Problem Dampener.

    Returns:
    --------
    int
        The number of safe reports
    """
    return sum(check_all_safe(test, try_remove_one).values())

assert check_all_safe(test=True)=={0: True, 1: False, 2: False, 3: False, 4: False, 5: True}
assert count_safe(test=True)==2

assert check_all_safe(test=True,try_remove_one=True)=={0: True, 1: False, 2: False, 3: True, 4: True, 5: True}
assert count_safe(test=True,try_remove_one=True)==4

print(count_safe(try_remove_one=True))
