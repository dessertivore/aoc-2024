"""
This was written on my phone and is still in note form!!
"""
dicto={}
for ycoord,line in enumerate(T.split("\n"),0):
    for xcoord,letter in enumerate(line,0):

        dicto[(xcoord,ycoord)]=letter
        if letter=="^":
            start=(xcoord,ycoord)


direction=(0,-1)
next=start
counter=1
D={(0,1):(-1,0),(1,0):(0,1),(0,-1):(1,0),(-1,0):(0,-1)}
print(next)
while next:
  
    if next not in dicto:
        break
    if dicto[next] != "#":
        
        if dicto[next]:
            counter+=1
        dicto[next]=False
        next=(next[0]+direction[0],next[1]+direction[1])
        
         
    else:
        next=(next[0]-direction[0],next[1]-direction[1])
        direction=D[direction]
        next=(next[0]+direction[0],next[1]+direction[1])
      
print(counter)