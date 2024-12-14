import math
import re

from matplotlib import pyplot as plt
from _common import get_input

numbers_reg = r'p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)'

class Robot:
    """
    Class to represent a robot in the grid.
    """
    def __init__(self,position:list,velocity:tuple):
        """
        Params:
        -------
        position: list
            List of two integers representing the x and y coordinates of the robot.
            This will be mutated, hence is not stored as a tuple like the velocity.

        velocity: tuple
            Tuple of two integers representing the x and y velocities of the robot.
        """
        self.position=position
        self.velocity=velocity
    
    def get_next_position(self, seconds:int =1,map_bounds:tuple=(101,103)):
        """
        Function to calculate the next position of the robot after a given number of 
        seconds, based on position and velocity. When the robot reaches the edge of the
        grid, it wraps around to the other side.

        Params:
        -------
        seconds: int
            Number of seconds to move the robot for. Default is 1.

        map_bounds: tuple
            Tuple of two integers representing the maximum x and y coordinates of the 
            grid. Default is (101,103).

        Returns:
        --------
        None (mutates self.position)
        """
        next:list[int,int]= [self.position[0]+(self.velocity[0]*seconds),self.position[1]+(self.velocity[1]*seconds)]
        for index in range(2):
            if next[index]<0:
                while next[index]<0:
                    next[index]+=map_bounds[index]
            elif next[index]>=map_bounds[index]:
                while next[index]>=map_bounds[index]:
                    next[index]-=map_bounds[index]
        self.position=next


def parse_input(test:bool=False) -> list[Robot]:
    """
    Parse the input data into a list of Robot objects.

    Params:
    -------
    test: bool
        If True, use test input. Default is False.

    Returns:
    --------
    list[Robot]
        List of Robot objects.
    """
    data= get_input(14,test)
    processed=[]
    for line in data.split("\n"):
        if line:
            nums=[int(y) for x in (re.findall(numbers_reg,line)) for y in x ]
            robot=Robot([nums[0],nums[1]],(nums[2],nums[3]))
            processed.append(robot)
    return processed

def move_robot(test:bool=False, seconds:int=1,current_map: list[Robot]|None=None):
    """
    Move robots in the grid for a given number of seconds and return the product of the 
    number of robots in each quadrant. If no map is given, starting positions from 
    puzzle input are used.

    Params:
    -------
    test: bool
        If True, use test input. Default is False.

    seconds: int
        Number of seconds to move the robots for. Default is 1.

    current_map: list[Robot]|None
        List of robots to move. If None, parse input data. Default is None.

    Returns:
    --------
    int
        Product of the number of robots in each quadrant.

    list[Robot]
        List of robots after moving for the given number of seconds.
    """
    if not current_map:
        current_map=parse_input(test)
    if not test:
        maxx=101
        maxy=103
    else:
        maxx=11
        maxy=7
    quadrant = [(int(maxx/2),y) for y in range(maxy+1)]
    otherline=[(x,int(maxy/2)) for x in range(maxx+1)]
    all_quadrant_middles=set(quadrant+otherline)
    robots_in_quadrant={"top_left":0,"top_right":0,"bottom_left":0,"bottom_right":0}
    for robot in current_map:
        if test:
            robot.get_next_position(seconds,(11,7))
        else:
            robot.get_next_position(seconds)
        if tuple(robot.position) in all_quadrant_middles:
            continue
        else:
            if robot.position[0]<=(maxx/2):
                if robot.position[1]<=(maxy/2):
                    robots_in_quadrant["top_left"]+=1
                else:
                    robots_in_quadrant["bottom_left"]+=1
            else:
                if robot.position[1]<=(maxy/2):
                    robots_in_quadrant["top_right"]+=1
                else:
                    robots_in_quadrant["bottom_right"]+=1
    total_prod=math.prod(robots_in_quadrant.values())
    return total_prod, current_map

assert move_robot(test=True,seconds=100)[0] == 12
print(move_robot(seconds=100)[0])

def part_2():
    """
    (Failed) attempt to visualize the robots moving in the grid in order to find the 
    Christmas tree.
    """
    from collections import deque 
    # Create an empty plot 
    fig, ax = plt.subplots() 
    line = ax.plot([]) 
    scatter = ax.scatter([], []) 

    # Set the x-axis and y-axis limits
    ax.set_xlim(0, 101) 
    ax.set_ylim(0, 103) 
  
    # Create a deque with fixed length 
    data_points = deque(maxlen=100) 
    
    def iter_robots():
        """
        Internal generator function to iterate over the robots' movements.
        """
        current_map=move_robot(test=False,seconds=0)[1]
        for x in range(10000):
            current_map=move_robot(test=False,seconds=x,current_map=current_map)[1]
            if len([tuple(y.position) for y in current_map])==len(set([tuple(y.position) for y in current_map])):
                # Check if all the robots are in different positions, if so 
                # print the iteration number and yield the current map to visualise
                print(x)
                yield x,current_map

    # Label graph with iteration number
    iteration_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
    
    for iteration,current_map in iter_robots():
        # Plot points in queue, with delay of 0.3s each (although likely will be longer
        # between iterations as not all iterations will be plotted)
        data_points.extend([x.position for x in current_map])      
        x_values = [x for x, y in data_points] 
        y_values = [y for x, y in data_points] 
        scatter.set_offsets(list(zip(x_values, y_values))) 
        iteration_text.set_text(f'Iteration: {iteration}')

        plt.pause(0.3)

plt.show()

part_2()