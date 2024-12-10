from collections import defaultdict
import math
from _common import get_input
import re

def parse_input(test: bool=False) -> tuple[list[tuple],list[list[int]]]:
    """
    Parse input for day 5.
    """
    raw=get_input(5,test).split("\n\n")
    page_order = [tuple(map(int, x.split("|"))) for x in re.findall(r"([0-9]{2}\|[0-9]{2})", raw[0])]    
    page_order_per_update = [[int(item) for item in sublist.split(",") if item] for sublist in raw[1].split("\n") if sublist]
    return page_order,page_order_per_update

def get_middle_index(update_list: list) -> int:
    middle_num=len(update_list)/2
    if middle_num % 2 != 0:
        middle_num-=0.5
    return int(middle_num)

def part_1(test: bool=False, part_2: bool=False) -> int:
    """
    Find the number of pages that are out of order.
    """
    page_order,page_order_per_update=parse_input(test)
    page_order_before_first:dict=defaultdict(lambda:[])
    page_order_after_first:dict=defaultdict(lambda:[])
    for before,after in page_order:
        page_order_before_first[before].append(after)
        page_order_after_first[after].append(before)
    safe_updates=0
    for update in page_order_per_update:
        if update==[75, 97, 47, 61, 53]:
            pass
        update_order_dict:dict=defaultdict(lambda:[])
        for x,y in enumerate(update,1):
            update_order_dict[y].append(x)
        safe_so_far=True
        
        for page_num,page in enumerate(update,1):
            if safe_so_far and (nums_must_come_after:=page_order_before_first.get(page)):
                for num_must_come_after in nums_must_come_after:
                    if safe_so_far and (indices_in_list:=update_order_dict.get(num_must_come_after)):
                        for index_in_list in indices_in_list:
                            if index_in_list > page_num:
                                safe_so_far=True
                            else:
                                safe_so_far=False
                                break

            if safe_so_far and (nums_must_come_before:=page_order_after_first.get(page)):
                for num_must_come_before in nums_must_come_before:
                    if safe_so_far and (indices_in_list:=update_order_dict.get(num_must_come_before)):
                        for index_in_list in indices_in_list:
                            if index_in_list < page_num:
                                safe_so_far=True
                            else:
                                safe_so_far=False
                                break
                        
        if safe_so_far:    
            middle_num=get_middle_index(update)
            safe_updates+=update[middle_num]


    return safe_updates
            


assert part_1(test=True)==143
print(part_1(test=False))