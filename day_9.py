from _common import get_input
from collections import defaultdict

def parse_input(test:bool=False) -> tuple[dict[int,dict],int]:
    """
    Parse today's input into a dictionary of dictionaries (containing indices, size of 
    files and free space), and the number of indices.
    """
    start: str = get_input(9,test)
    x: int=0
    y: int =1
    idindex: int=0
    pairs: dict[int,dict]=defaultdict(lambda:{"file":0,"free":[0,[]]})
    while x<len(start):
        if start[x]!="\n":
            pairs[idindex]["file"]=int(start[x])
            if y in range(len(start)) and start[y]!="\n":
                pairs[idindex]["free"][0]=int(start[y])
            y+=2
            x+=2
            idindex+=1
    return pairs, idindex

def calculate_checksum(files:list) -> int:
    """
    Multiply each number by its position in a string (in form of a list, to preserve
    multi-digit numbers) and return sum.

    Params:
    -------
    files: list
        List of numbers in string form.

    Returns:
    --------
    int
        Checksum of the list of numbers.
    """
    check=0
    for num,digit in enumerate(files,0):
        if digit!=".":
            check+=int(digit)*num
    return check

def rearrange_files(test:bool=False, part_2:bool=False) -> int:
    """
    Gets a string of file information, and rearranges the files to fill up as much
    free space in lower indices as possible.
    For part_2, it will rearrange the files to fill up as much free space in lower indices
    as possible but only if all files from the current index can fit in the free space
    together.
    Checksum of resulting file information is returned.

    Params:
    -------
    test: bool
        Whether to use test data or not.

    part_2: bool
        Whether to use part 2 logic or not.

    Returns:
    --------
    int
        Checksum of the resulting file information.
    """

    pairs,idindex=parse_input(test)

    max=idindex
    freeindex=0
    has_space=[x for x in range(max)]
    for idx in reversed(range(idindex+1)):
    # print(idx,pairs[idx])
        has_space_index=0 
        while pairs[idx]["file"]>0:
        
            if not part_2:
                if freeindex<idx:
                    if pairs[freeindex]["free"][0]>0:
            
                        pairs[freeindex]["free"][0]-=1
                        pairs[idx]["file"]-=1
                        pairs[idx]["free"][1].append(".")
                        pairs[freeindex]["free"][1].append(str(idx))
                    else:
                        freeindex+=1
                else:
                    break
            else:
                free=has_space[has_space_index]
                if free<idx:
                    if pairs[free]["free"][0]>=pairs[idx]["file"]:
                        pairs[free]["free"][0]-=pairs[idx]["file"]
                        pairs[free]["free"][1].extend([str(idx) for x in range(pairs[idx]["file"])])
                        if pairs[free]["free"][0]==0:
                            has_space.pop(has_space_index)
                        pairs[idx]["free"][1]=["." for x in range(pairs[idx]["file"])]+pairs[idx]["free"][1]+["." for x in range(pairs[idx]["free"][0])]
                        pairs[idx]["file"]=0
                        break
                        
                    else:
                        has_space_index+=1
        
                    
                else:
                    pairs[idx]["free"][1]=pairs[idx]["free"][1]+["." for x in range(pairs[idx]["free"][0])]
                    break
    full=[]

    for id,info in pairs.items():

        for x in range(info["file"]):
            full.append(str(id))
        for n in info["free"][1]:
            full.append(n)

    return calculate_checksum(full)
    
        
assert rearrange_files(test=True) == 1928
assert rearrange_files(test=True, part_2=True) == 2858

print(rearrange_files(part_2=True))