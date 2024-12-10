"""
This was written on my phone and is still in note form!!
"""
from collections import defaultdict

from _common import get_input

start=get_input(8,test=False)
part2=True
coorddict=defaultdict(lambda:[])
maxy=0
maxx=0
for ycoord,line in enumerate(start.split("\n")):
    for xcoord,char in enumerate(line,0):
        if char !=".":
            coorddict[char].append((xcoord,ycoord))
        if xcoord>maxx:
            maxx=xcoord
        if ycoord >maxy:
            maxy=ycoord
antinodes=set()
all={x for coords in coorddict.values() for x in coords}
for frequency,coordlist in coorddict.items():
        for ind,coord in enumerate(coordlist,1):
            for coord2 in coordlist[ind:]:
             
                diff=(lambda x,y:(x[0]-y[0],x[1]-y[1]))(coord,coord2)
              
                antinodeslist=[(lambda x,y:(x[0]-y[0],x[1]-y[1]))(coord2,diff),(lambda x,y:(x[0]+y[0],x[1]+y[1]))(coord,diff)]
                if part2:
                    flag=True
                    x=0
                    y=1
                    while flag:
                       
                        c1=antinodeslist[x]
                        c2=antinodeslist[y]
                        print(c1,c2)
                        if c1[0] in range(maxx+1) and c1[1] in range(maxy+1):
                            antinodeslist.append((lambda x,y:(x[0]-y[0],x[1]-y[1]))(c1,diff))
                            x+=1
                            flag=True
                        else:
                            flag=False
                  
          
                        if c2[0] in range(maxx+1) and c2[1] in range(maxy+1):
                            
                            antinodeslist.extend([(lambda x,y:(x[0]+y[0],x[1]+y[1]))(c2,diff)])
                            y+=1
                            flag=True
                        else:
                            flag=False
                        print(flag)
                          
                print(antinodeslist,frequency,coord,coord2)            
                for antinode in antinodeslist:
    
                    if antinode[0] in range(maxx+1) and antinode[1] in range(maxy+1):
                        antinodes.add(antinode)
                   
print(len(antinodes))