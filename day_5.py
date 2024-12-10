import math
from _common import get_input
import re

def parse_input(test: bool=False) -> tuple[list[tuple],list[list[int]]]:
    """
    Parse input for day 5.
    """
    raw=get_input(5,test).split("\n\n")
    page_order = [tuple(map(int, x.split("|"))) for x in re.findall(r"([0-9]{2}\|[0-9]{2})", raw[0])]    
    page_order_per_update = [[int(item) for item in sublist.split(",") if item] for sublist in raw[1].split("\n")]
    return page_order,page_order_per_update

def part_1(test: bool=False) -> int:
    """
    Find the number of pages that are out of order.
    """
    page_order,page_order_per_update=parse_input(test)
    page_order_dict={x:y for x,y in page_order}
    safe_updates=0
    for update in page_order_per_update:
        update_order_dict={y:x for x,y in enumerate(update,1)}
        safe_so_far=True
        for page in update:
            if num_must_come_after:=page_order_dict.get(page):
                if index_in_list:=update_order_dict.get(num_must_come_after):
                    if index_in_list > update_order_dict[page]:
                        safe_so_far=True
                    else:
                        safe_so_far=False
                        break
        if safe_so_far:
            
            middle_num=int(len(update)/2)
            print(middle_num,len(update))
            safe_updates+=update[middle_num]
    return safe_updates
            


assert part_1(test=True)==143
print(part_1())