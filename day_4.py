
from _common import get_input

def parse_input(test: bool=False) -> list:
    lines = get_input(4,test)
    return lines.split("\n")

def xmas_wordsearch(test: bool=False) -> int:
    lines=parse_input(test)
    output={}
    for ycoord,line in enumerate(lines,0):
       for xcoord, letter in enumerate(line,0):
           output[(xcoord,ycoord)]= letter
    counter=0
    for coords,letter in output.items():
        if letter=="X":
            for direction in [(x,y) for x in range(-1,2) for y in range(-1,2) if (x,y) != (0,0)]:
                current=coords
                for next in "MAS":
                    current=(lambda x, y: (x[0]+y[0],x[1]+y[1]))(current,direction)
                    if output.get(current) != next:
                        break
                    if next == "S":
                        counter+=1
    return counter  
                   
assert xmas_wordsearch(test=True) == 18

print(xmas_wordsearch())
