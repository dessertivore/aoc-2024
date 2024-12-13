from _common import get_input
from shapely import Polygon, MultiPolygon
from collections import defaultdict

def create_square_around_coord(x:int,y:int) -> Polygon:
    """
    Create a square around a coordinate.
    """
    return Polygon([(x+0.5,y),(x-0.5,y),(x,y+0.5),(x,y-0.5)])

def parse_input(test: bool=False) -> dict:
    """
    Parse input for day 12.
    """
    lines = get_input(12,test).split("\n")
    map:dict=defaultdict(lambda:[])
    for ycoord,line in enumerate(lines,0):
       for xcoord, letter in enumerate(line,0):
           map[letter].append(create_square_around_coord(xcoord,ycoord))
    return map

def create_multipoly(test: bool=False) -> MultiPolygon:
    """
    Create a polygon from the input data.
    """
    map=parse_input(test)
    polygons_dict:dict={}
    for key,polygons in map.items():
        polygons_dict[key]=MultiPolygon(polygons)
    return polygons

def calculate(test: bool=False) -> int:
    """
    Calculate the area of the polygon.
    """
    polygons=create_multipoly(test)
    print(polygons)
    total =0
    for poly in polygons:
        print(poly.area)
        total+=(poly.area)
    return total

print(calculate(test=True))