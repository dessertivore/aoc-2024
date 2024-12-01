

from collections import defaultdict
from _common import get_input

def parse_input(test=False):
    data=get_input(1,test)
    return [x.split("   ") for x in (data.split("\n")) if x.split("   ") != ['']]

def sort_by_x_value_in_list(data):
    return sorted(data,key=lambda x:x[0])

def sort_by_y_value_in_list(data):
    return sorted(data,key=lambda x:x[1])

def sort_all(test:bool=False):
    data=parse_input(test)
    sorted_by_x= sort_by_x_value_in_list(data)
    sorted_by_y= sort_by_y_value_in_list(data)
    new_data=[]
    for x,y in zip(sorted_by_x,sorted_by_y):
        new_data.append([int(x[0]), int(y[1])])
    return new_data
        
def distance_apart(test:bool=False):
    data=sort_all(test)
    return sum([abs(x-y) for x,y in data])

assert distance_apart(test=True) == 11
print(distance_apart())

def similarity_score(test:bool=False):
    data=sort_all(test)
    appearances: dict=defaultdict(lambda:0)
    similarity_score=0
    for x,y in data:
        appearances[y] +=1
    for x,y in data:
        if appearances[x] >= 1:
            similarity_score+= appearances[x]*x
    return similarity_score

assert similarity_score(test=True) == 31
print(similarity_score())
        