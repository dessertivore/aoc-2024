"""
This was written on my phone and is still in note form!!
"""
import math
def con(nums):
    out=""
    for num in nums:
        out+=str(num)
    return(int(out))
operators=[sum,math.prod,con]

import re
start=actual

out=[]
for line in start.split("\n"):
    chars=re.findall(r"[0-9]*",line)
    out.append({int(chars[0]): [int(x) for x in chars[1:] if x]})


counter=0
for ldict in out:
  
    val,equation=list(ldict.items())[0]
    #print(val)
   
    if sum(equation) == val or math.prod(equation)==val or con(equation)==val:
        counter+=val
        continue
    def try_operator(l):
        if len(l)==2:
            #print(l)
            return [op(l) for op in operators]
        poss=[]
        for op in operators:
            c=op(l[:2])
     
            new=l[2:]
            new.insert(0,c)
          
         
            poss.extend(try_operator(new))
      
        return poss
            
    possibilities= try_operator(l=equation)
    #print(possibilities)
    if val in possibilities:    
        counter+=val
print(counter)