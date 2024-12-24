from _common import get_input


OPERATORS:dict={"AND":lambda x,y: 1 if x+y==2 else 0, "OR":lambda x,y: 1 if (x+y) in [1,2] else 0,"XOR":lambda x,y: 1 if x+y==1 else 0}

class Gate:    
    def __init__(self,info:str):
        info_list:list=info.split(" ")
        self.info=info
        self.wires=tuple([info_list[0],info_list[2]])
        self.operator=OPERATORS[info_list[1]]
        self.write_to=info_list[4]

    def __repr__(self) -> str:
        return self.info
    
def parse_input(test:bool=False):
    data=get_input(24,test).split("\n\n")
    wires=data[0].splitlines()
    wires_dict: dict={}
    for wire in wires:
        wire=wire.split(": ")
        wires_dict[wire[0]]=int(wire[1])
    
    gates=data[1].splitlines()
    all_gates:list[Gate]=[]
    for gate in gates:
        all_gates.append(Gate(gate))    
    return wires_dict,all_gates

def parse_gates(test:bool=False):
    wires, gates=parse_input(test)
    z_wires:str=""
    while gates:
        gate=gates.pop(0)
        try:
            output=gate.operator(*tuple(wires[wire] for wire in gate.wires))
            wires[gate.write_to]=output
        except KeyError:
            gates.append(gate)
    sorted_wires = sorted(wires,reverse=True)
    for wire in sorted_wires:
        if wire[0]=="z":
            z_wires+=str(wires[wire])
    return int(z_wires,2)

assert parse_gates(test=True) == 2024
print(parse_gates(test=False))