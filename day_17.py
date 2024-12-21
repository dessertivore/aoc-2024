from _common import get_input

NUM_TO_ACTION:dict={
    0: lambda x,y:int(x/pow(2,y)), # written to the A register.
    1: lambda x,y: x&y, # write to B
    2: lambda x,y: x%8, # write to B
    3: lambda x,y: x if y != 0 else 0, # where A is 0, x is literal operand, and this jumps the pointer
    4: lambda x,y: x&y, # where x and y are B and C, and stored in B. Reads an operand but ignores
    5: lambda x,y: x%8, # where x is combo operand calculates the value of its combo operand, comma separated
    6: lambda x,y:int(x/pow(2,y)), # written to B, numerator is A
    7: lambda x,y:int(x/pow(2,y)) # written to C, numberator is A
    }

COMBO_OPERANDS:dict={
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: "A",
    5: "B",
    6: "C",
    7: "ERROR"
}
NUM_TO_X_Y:dict={
    0: ("A","COMBO"),
    1: ("B","LITERAL"),
    2: ("COMBO",None),
    3: ("A","LITERAL"),
    4: ("B","C"),
    5: ("COMBO",None),
    6: ("A","COMBO"),
    7: ("A","COMBO")
}

NUM_TO_STORAGE_LOCATION:dict={
    0: "A",
    1: "B",
    2: "B",
    3: None,
    4: "B",
    5: "OUT",
    6: "B",
    7: "C"
}

def parse_input(test:bool=False):
    registers, program = tuple(get_input(17,test).split("\n\n"))
    all_registers = {}
    for register in registers.split("\n"):
        register=register.replace("Register ", "").split(":")
        all_registers[register[0]] = int(register[1])
    program = [int(x) for x in program.replace("Program: ","").split(",")]
    return all_registers,program

def run_program(test:bool=False):
    registers,program=parse_input(test)
    pointer = 0
    while pointer< len(program):
        action=program[pointer]
        operand=program[pointer+1]
        subjects=NUM_TO_X_Y[action]
        for subject in subjects:
            if subject
        save_to=NUM_TO_STORAGE_LOCATION[action]
        result=NUM_TO_ACTION[action](operand,operand)
print(parse_input(test=True))