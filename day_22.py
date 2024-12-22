from _common import get_input

def parse_input(test:bool=False):
    """
    Parse input.

    Params:
    -------
    test: bool
        Whether to use test data or not.

    Returns:
    --------
    list[int]
        List of integers.
    """
    data=get_input(22,test)
    output=[]
    for line in data.split("\n"):
        if not line:
            continue
        output.extend(int(x) for x in line.split(" "))
    return output

def mix(secret:int, num:int)-> int:
    """Get bitwise XOR for secret and num."""
    return num ^ secret

assert mix(42,15)==37

def prune(secret:int)-> int:
    """Prune secret by calculating modulo 16777216."""
    return secret % 16777216

assert prune(100000000) == 16113920

def steps_to_secret(test:bool=False, first_secrets:list[int]|None=None) -> list:
    """
    Transform secret numbers using set steps, to get new secret numbers.
    """
    if first_secrets:
        data=first_secrets
    else:
        data=parse_input(test)
    new_secrets:list=[]
    for secret in data:
        secret=prune(mix(secret,int(64*secret)))
        secret=prune(mix(secret,int(secret/32)))
        secret=prune(mix(secret,secret*2048))
        new_secrets.append(secret)
    return new_secrets

assert steps_to_secret(test=True, first_secrets=[123])[0] == 15887950

def repeat_steps(test:bool=False, first_secrets:list[int]|None=None, steps:int=1):
    """
    Repeat the steps to get the final secret numbers for the banana buyers.
    """
    secrets=steps_to_secret(test, first_secrets)
    for _ in range(steps-1):
        secrets=steps_to_secret(test,secrets)
    return secrets

assert repeat_steps(test=True, first_secrets=[123], steps=10) == [
    5908254
]

assert repeat_steps(test=True,steps=2000)==[8685429, 4700978, 15273692, 8667524]

def sum_steps(test:bool=False, steps:int=2000):
    """
    Get sum of all the final secret numbers.
    """
    final_secrets=repeat_steps(test,steps=steps)
    return sum(final_secrets)

assert sum_steps(test=True) == 37327623

# print(sum_steps())

def get_consecutive_changes(test:bool=False,steps:int=2000,first_secrets:list|None=None):
    """
    Start of part 2 of the problem.
    Need to get final number of each secret for each step and then get the difference 
    between the final numbers. Will then need to find the best pattern to optimise
    banana buying.
    """
    if first_secrets:
        current_secrets=first_secrets
    else:
        current_secrets=steps_to_secret(test)
    final_nums:list=[int(str(x)[-1]) for x in current_secrets]
    differences=[]
    for x in range(1,steps):
        new_secrets=steps_to_secret(test,first_secrets=current_secrets)
        new_final_nums=[int(str(x)[-1]) for x in current_secrets]
        differences.append([new_final_nums[i]-final_nums[i] for i in range(len(final_nums))])
        final_nums.append(new_final_nums)
        current_secrets=new_secrets
        final_nums=new_final_nums
    return differences,final_nums

assert get_consecutive_changes(test=True,steps=10,first_secrets=[123])[0]==[[0], [-3], [6], [-1], [-1], [0], [2], [-2], [0]]

print(get_consecutive_changes(test=True,steps=10,first_secrets=[1,2,3,2024])[1])