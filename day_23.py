from collections import defaultdict
from _common import get_input

def parse_input(test:bool=False):
    connections:dict=defaultdict(lambda:[])
    for line in get_input(23,test).splitlines():
        first,second=tuple(line.split("-"))
        connections[first].append(second)
        connections[second].append(first)
    return connections

def find_connections(test:bool=False):
    connections = parse_input(test)
    full_sets:set=set()
    for first_comp,connected in connections.items():
        for idx1 in range(len(connected)):
            compare_1:str=connected[idx1]
            for idx2 in range(1,len(connected)-1):
                compare_2:str=connected[idx2]
                if compare_2 in connections[compare_1]:
                    # Sort and add to set so that duplicates are not added
                    full_sets.add(tuple(sorted([first_comp,compare_1,compare_2])))
    return full_sets

assert len(find_connections(test=True))==12

def find_sets_with_t(test:bool=False):
    sets_of_three:set=find_connections(test)
    possibly_chief:list=[]
    for triplet in sets_of_three:
        for computer in triplet:
            if computer[0]=="t":
                possibly_chief.append(triplet)
                break
    return len(possibly_chief)


assert find_sets_with_t(test=True) == 7
# print(find_sets_with_t(test=False))

class LANGraph():
    #  This is graph code I found online
    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertex):
        """ returns a list of all the edges of a vertex"""
        return self._graph_dict[vertex]
        
    def all_vertices(self):
        """ returns the vertices of a graph as a set """
        return set(self._graph_dict.keys())

    def all_edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self._graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].add(y)
            else:
                self._graph_dict[x] = [y]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    
    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj
    
    def __next__(self):
        """ allows us to iterate over the vertices """
        return next(self._iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
    


def parse_input_2(test:bool=False):
    connections:dict=defaultdict(lambda:[])
    for line in get_input(23,test).splitlines():
        first,second=tuple(line.split("-"))
        connections[first].append(second)
        connections[second].append(first)
    return LANGraph(connections)

graph=parse_input_2(test=True)

def find_most_connections(test:bool=False):
    # Will need to do some graph connections algorithm here
    graph=parse_input_2(test)
    max_num:int=0
    max_edge:str=""
    for vertex in graph.all_vertices():
        if len(graph.edges(vertex)) > max_num:
            max_num=len(graph.edges(vertex))
            max_edge=vertex
    return max_num,max_edge
