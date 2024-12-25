from collections import defaultdict
from _common import get_input

class LockOrKey:
    """
    Class to keep track of Locks and Keys.
    """
    instance_count:int = 0  # Class variable to keep track of the instance count
    key_to_code:dict = defaultdict(lambda:None)  # Class variable to keep track of which code corresponds to which instance
    lock_to_code:dict = defaultdict(lambda:None)  # Class variable to keep track of which code corresponds to which instance
    all_instances:dict = {}  # Class variable to keep track of all instances

    def __init__(self,info:dict):
        self.map=info
        self.first_row=set([self.map[(x,0)] for x in range(5)])
        if self.first_row=={"#"}:
            self.definition="LOCK"
        elif self.first_row=={"."}:
            self.definition="KEY"
        else:
            raise ValueError("Invalid Lock or Key {} {} {}".format(self.map,5,6))

        # Increment the instance count and assign a unique number to this instance
        self.instance_number = LockOrKey.instance_count
        LockOrKey.instance_count += 1
        
    def calculate_columns(self):
        code=""
        if self.definition == "KEY":
            curr_y=6
            reversed=True
        else:
            curr_y=0
            reversed=False

        for x in range(5):
            new_y=curr_y
            while self.map.get((x,new_y))=="#":
                if reversed:
                    new_y-=1
                else:
                    new_y+=1
            if reversed:
                code+=str(6-new_y-1)
            else:
                code+=str(new_y-1)
        if self.definition=="LOCK":
            LockOrKey.lock_to_code[self.instance_number]=code
        elif self.definition=="KEY":
            LockOrKey.key_to_code[self.instance_number]=code
        else:
            raise ValueError("Invalid Lock or Key {} {} {}".format(self.map,4,6))
        LockOrKey.all_instances[self.instance_number]=self
        self.code=code
        return code


def parse_input(test:bool=False) -> list[LockOrKey]:
    """
    Parse raw input.

    Params:
    -------
    test:
        bool: Test flag to use test data.

    Returns:
    --------
    all_locks_or_keys:
        list[LockOrKey]: List of all Locks and Keys.
    """
    raw=get_input(25,test).split("\n\n")
    maxx=1
    maxy=1
    all_locks_or_keys=[]
    for key_or_lock in raw:
        current_dict:dict={}
        for ycoord,line in enumerate(key_or_lock.splitlines()):
            for xcoord, char in enumerate(line):
                if xcoord>maxx:
                    maxx=xcoord
                if ycoord>maxy:
                    maxy=ycoord
                current_dict[(xcoord,ycoord)]=char
        all_locks_or_keys.append(LockOrKey(current_dict))
    return all_locks_or_keys

def get_codes(test:bool=False):
    """
    Calculate all the codes for each lock and key.
    Iterate over them all and check if they overlap or if they fit.
    Return number of keys/locks that fit.

    Params:
    -------
    test:
        bool: Test flag to use test data.

    Returns:
    --------
    counter:
        int: Number of keys/locks that fit.
    """
    all_locks_or_keys:list[LockOrKey]=parse_input(test)
    for lock_or_key in all_locks_or_keys:
        lock_or_key.calculate_columns()

    counter=0
    for lock,lock_code in LockOrKey.lock_to_code.items():
        for key,key_code in LockOrKey.key_to_code.items():
            overlap=False
            for idx in range(len(lock_code)):
                if int(key_code[idx])+int(lock_code[idx]) > 5:
                    overlap=True
                    break
            if not overlap:
                counter+=1
                continue

    return counter

# assert get_codes(test=True) ==3
print(get_codes())