from collections import defaultdict
from _common import get_input
import re

def parse_input(test: bool=False) -> tuple[list[tuple],list[list[int]]]:
    """
    Parse input for day 5.

    Params:
    -------
    test: bool
        Whether to use test input.

    Returns:
    --------
    tuple
        Tuple of page order constraints and page order in each update.
    """
    raw=get_input(5,test).split("\n\n")
    page_order_constraints = [tuple(map(int, x.split("|"))) for x in re.findall(r"([0-9]{2}\|[0-9]{2})", raw[0])]    
    page_order_per_update = [[int(item) for item in sublist.split(",") if item] for sublist in raw[1].split("\n") if sublist]
    return page_order_constraints,page_order_per_update

def get_middle_index(update_list: list) -> int:
    """
    Get the middle index of a list.

    Params:
    -------
    update_list: list
        List of pages in update.

    Returns:
    --------
    int
        Middle index.
    """
    middle_num=len(update_list)/2
    if middle_num % 2 != 0:
        middle_num-=0.5
    return int(middle_num)

def find_updates_out_of_order(test: bool=False, part_2: bool=False) -> tuple[int,list]:
    """
    Find the number of updates that are out of order.

    If part_2 is True, build a list of unordered updates. An empty list will be returned
    in its place if part_2 is False.

    Params:
    -------
    test: bool
        Whether to use test input.

    part_2: bool
        Whether to create list of unordered updates or return empty list in its place.

    Returns:
    --------
    tuple[int,list]
        Tuple of number of safe updates and list of unordered updates.
    """
    page_order,page_order_per_update=parse_input(test)
    page_order_before_first:dict=defaultdict(lambda:[])
    page_order_after_first:dict=defaultdict(lambda:[])
    unordered_updates=[]
    for before,after in page_order:
        page_order_before_first[before].append(after)
        page_order_after_first[after].append(before)
    safe_updates=0
    for update in page_order_per_update:
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
                                if part_2:
                                    unordered_updates.append(update)
                                break

            if safe_so_far and (nums_must_come_before:=page_order_after_first.get(page)):
                for num_must_come_before in nums_must_come_before:
                    if safe_so_far and (indices_in_list:=update_order_dict.get(num_must_come_before)):
                        for index_in_list in indices_in_list:
                            if index_in_list < page_num:
                                safe_so_far=True
                            else:
                                safe_so_far=False
                                if part_2:
                                    unordered_updates.append(update)
                                break
                        
        if safe_so_far:    
            middle_num=get_middle_index(update)
            safe_updates+=update[middle_num]


    return safe_updates,unordered_updates
            

def apply_constraints(wrongly_ordered: list, constraints: dict) -> list:
    """
    Bubble sort, using dict of constraints to dictate orter.

    Params:
    -------
    wrongly_ordered: list
        List of wrongly ordered updates.

    constraints: dict
        Dict of constraints. In format {page: [pages that must come after page]}

    Returns:
    --------
    list
        List of updates with pages in correct order.
    """
    changed = True
    while changed:
        changed = False
        for i in range(len(wrongly_ordered) - 1):
            for key, values in constraints.items():
                if wrongly_ordered[i] == key and wrongly_ordered[i + 1] in values:
                    # Swap elements to satisfy the constraint
                    wrongly_ordered[i], wrongly_ordered[i + 1] = wrongly_ordered[i + 1], wrongly_ordered[i]
                    changed = True
    return wrongly_ordered

def fix_page_order(test: bool=False) -> int:
    """
    Get wrongly ordered updates, fix the page order and sum middle numbers.

    Params:
    -------
    test: bool
        Whether to use test input.

    Returns:
    --------
    int
        Sum of middle numbers.
    """
    page_order,page_order_per_update=parse_input(test)
    page_order_before_first:dict=defaultdict(lambda:[])
    for before,after in page_order:
        page_order_before_first[before].append(after)
    middle_nums=[]
    for update in find_updates_out_of_order(test=test,part_2=True)[1]:
        fixed_update=apply_constraints(update,page_order_before_first)
        middle_nums.append(fixed_update[get_middle_index(fixed_update)])
    return sum(middle_nums)

assert fix_page_order(test=True)==123
# print(fix_page_order(test=False))