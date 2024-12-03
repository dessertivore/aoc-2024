import re 
import math

from _common import get_input

def match(text: str, with_dos_and_donts:bool=False) -> int:
    """
    For a given string, find all instances of the pattern mul(x,y) and return the sum 
    of the products of x and y.

    Params:
    -------
    text: str
        The text to search through.
    with_dos_and_donts: bool
        Whether to ignore all instances of do() and don't() or not. If True, when do()
        is found, subsequent mul() instances will be used until don't() is found, after
        which they will be ignored, and so on.
    """
    output=0
    matches: list= re.findall(r'''mul\([0-9]*,[0-9]*\)|do\(\)|don't\(\)''',text)
    ignore: bool=False
    for match in matches:
        if with_dos_and_donts:
            if match == "do()":
                ignore=False
            elif match == "don't()":
                ignore=True
            if ignore:
                continue
        nums=[int(x) for x in (re.findall(r'[0-9]*',match)) if x]
        if nums: # Need this line as if nums is empty, math.prod(nums) will return 1
            output+=math.prod(nums)
    return output

assert match(get_input(3,test=True)) == 161
assert match(get_input(3,test= True),with_dos_and_donts=True) == 48

print(match(get_input(3),with_dos_and_donts=True))