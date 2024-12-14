import re
from _common import get_input

input_pattern = r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)'

A_COST=3
B_COST=1

class ClawMachineInput:
    def __init__(self,AX: int, AY: int, BX:int, BY: int, PrizeX:int, PrizeY:int):
        self.AX = int(AX)
        self.AY = int(AY)
        self.BX = int(BX)
        self.BY = int(BY)
        self.Prize = (int(PrizeX), int(PrizeY))
        self.A=(self.AX,self.AY)
        self.B=(self.BX,self.BY)

def parse_input(test:bool=False) -> list[ClawMachineInput]:
    data=get_input(13,test)
    all_data: list[ClawMachineInput]=[]
    for input in re.findall(input_pattern,data):
        all_data.append(ClawMachineInput(*input))
    return all_data

def press_button(VISITED:set,current: tuple, button: tuple, machine: ClawMachineInput, prize:tuple, spent_so_far:int,cost:int=1) -> int:
    next = (current[0]+button[0],current[1]+button[1])
    if next in VISITED:
        return float("inf")
    if next== prize:
        return cost + spent_so_far
    elif next[0] > prize[0] or next[1] > prize[1]:
        return float("inf")
    else:
        VISITED.add(next)
        return min(press_button(VISITED,next,machine.A,machine,prize,spent_so_far+cost,A_COST),press_button(VISITED,next,machine.B,machine,prize,spent_so_far+cost,B_COST))
        
def claw_machine(test:bool=False,part_2:bool=False) -> list:
    data=parse_input(test)
    min_cost=[]
    for machine in data:
        VISITED=set()
        prize=machine.Prize
        if part_2:
            # loop through powers of 10 until minimum one is found

            total=min(press_button(VISITED,(0,0),machine.A,machine,prize,0,A_COST),press_button(VISITED,(0,0),machine.B,machine,prize,0,B_COST))
        total=min(press_button(VISITED,(0,0),machine.A,machine,prize,0,A_COST),press_button(VISITED,(0,0),machine.B,machine,prize,0,B_COST))
        min_cost.append(total)
    return min_cost

def get_min_cost(test:bool=False, part_2:bool=False) -> int:
    if part_2:
        divisible_by_10, cost=claw_machine(test,True)
        (10000000000000/divisible_by_10)
    return sum([x for x in claw_machine(test,part_2) if x!=float('inf')])

# assert claw_machine(test=True) == [280,float('inf'),200,float('inf')]
# assert get_min_cost(test=True) == 480
print(get_min_cost(test=True,part_2=True))