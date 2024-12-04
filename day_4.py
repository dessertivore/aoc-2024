
from _common import get_input

def parse_input(test: bool=False) -> list:
    """
    Parse input for day 4.
    """
    lines = get_input(4,test)
    return lines.split("\n")

def xmas_wordsearch(test: bool=False, check_crosses: bool=False) -> int:
    """
    Find the number of times the word "XMAS" appears in the wordsearch.
    If check_crosses is True, find the number of times the X-"MAS" appears in the 
    wordsearch.

    Params:
    -------
    test: bool
        Whether to use test data or not.

    check_crosses: bool
        Whether to check for X-"MAS" or not. If set to False, then searches for "XMAS".
    """
    lines=parse_input(test)

    output={}
    for ycoord,line in enumerate(lines,0):
       for xcoord, letter in enumerate(line,0):
           output[(xcoord,ycoord)]= letter
    counter=0
    for coords,letter in output.items():
        if not check_crosses:
            if letter=="X":
                for direction in [(x,y) for x in range(-1,2) for y in range(-1,2) if (x,y) != (0,0)]:
                    current=coords
                    for next in "MAS":
                        current=(lambda x, y: (x[0]+y[0],x[1]+y[1]))(current,direction)
                        if output.get(current) != next:
                            break
                        if next == "S":
                            counter+=1
        else:
            if letter=="A":
                flag=False
                for directions in [((-1,-1),(1,1)),((1,-1),(-1,1))]:
                    diagonals =[(lambda x, y: (x[0]+y[0],x[1]+y[1]))(coords,d) for d in directions]
                    if all([output.get(diagonals[0]) == "M", output.get(diagonals[1]) == "S"]) or all([output.get(diagonals[0]) == "S", output.get(diagonals[1]) == "M"]):
                        flag=True
                    else:
                        flag=False
                        break
                if flag:
                    counter+=1

    return counter  
                   
assert xmas_wordsearch(test=True) == 18
assert xmas_wordsearch(test=True,check_crosses=True) == 9
print(xmas_wordsearch(check_crosses=True))
