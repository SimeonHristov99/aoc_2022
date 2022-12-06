import numpy as np
lines = open("input(ivaka).txt").read().splitlines()

lines=np.asarray(lines)

the_max=0
buffer=[]
for num in lines:
    if num=="":
        the_max=max(the_max,sum(buffer))
        print(buffer)
        buffer=[]

    else:
        buffer.append(int(num))


print(the_max)