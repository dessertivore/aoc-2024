from _common import get_input

def parse_input(test:bool=False):
    data=get_input(22,test)
    output=[]
    for line in data.split("\n"):
        if not line:
            continue
        output.extend(int(x) for x in line.split(" "))
    return output

def mix(secret:int, num:int)-> int:
    return num ^ secret

assert mix(42,15)==37

def prune(secret:int)-> int:
    return secret % 16777216

assert prune(100000000) == 16113920

def steps_to_secret(test:bool=False, first_secrets:list[int]|None=None) -> list:
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
    secrets=steps_to_secret(test, first_secrets)
    for _ in range(steps-1):
        secrets=steps_to_secret(test,secrets)
    return secrets

assert repeat_steps(test=True, first_secrets=[123], steps=10) == [
    5908254
]

assert repeat_steps(test=True,steps=2000)==[8685429, 4700978, 15273692, 8667524]

def sum_steps(test:bool=False, steps:int=2000):
    final_secrets=repeat_steps(test,steps=steps)
    return sum(final_secrets)

assert sum_steps(test=True) == 37327623

print(sum_steps())