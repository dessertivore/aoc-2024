from collections import defaultdict
from itertools import cycle
from _common import DIRECTIONS, get_input

def parse_input(test:bool=False):
    data=get_input(16,test)
    reindeer_olympics_map:dict=defaultdict(lambda:None)
    for y,line in enumerate(data.splitlines()):
        for x,char in enumerate(line):
            if char=='#':
                reindeer_olympics_map[(x,y)]="#"
            elif char=='E':
                reindeer_olympics_map[(x,y)]="E"
            elif char=='S':
                start=(x,y)
    return reindeer_olympics_map, start


def reindeer_bfs(start:tuple,olympics_map:dict):
    visited:dict=dict()
    queue=[(start,0, 2,2),(start,0, 3,2),(start,0, 1,2)]
    min_score=float("inf")
    while queue:
        location, score,dir_index,prev_dir_index=queue.pop(0)
        next_loc=(DIRECTIONS[dir_index][0]+location[0],DIRECTIONS[dir_index][1]+location[1])
        if (visited.get(next_loc,float("inf"))<=score)  or olympics_map[next_loc]=="#":
            continue
        if olympics_map[next_loc]=="E":
            min_score=min(min_score,score+1+(1000 if dir_index!=prev_dir_index else 0))
            continue
        visited[next_loc]=score
        next_score = score + 1 + (1000 if dir_index != prev_dir_index else 0)

        for next_dir in [dir_index, (dir_index - 1) % 4, (dir_index + 1) % 4]:
            queue.append((next_loc,next_score, next_dir, dir_index))
    return min_score

def find_best_path(test:bool=False):
    reindeer_olympics_map, start =parse_input(test)
    return reindeer_bfs(start,reindeer_olympics_map)

print(find_best_path(False))
assert find_best_path(True) == 11048
