import re
def solution(lines,part):
    columns=lines[:lines.index("")]
    last=columns[len(columns)-1]
    the_big_arr=[]
    for i in range(0,int(last[len(last)-2])):
        the_big_arr.append([])
        
    prev=0
    index=0
    t=1
    upper=3

    for j in range(0, len(columns)):
        for i in range(0,len(columns[j])+1):
         
           if i==upper:
                if not columns[j][prev:i].isspace():
                    the_big_arr[index].append(columns[j][prev:i])
                index+=1
                prev=i
                prev+=t
                upper=prev+3
        prev=0
        index=0
        t=1
        upper=3
        
    movements=lines[lines.index("")+1:]
    for movement in movements:
        x = re.findall('[0-9]+', movement)
        move=int(x[0])
        _from=int(x[1])-1
        to=int(x[2])-1
        buffer=the_big_arr[_from][:move]
        if part=="1":
            buffer.reverse()
        the_big_arr[to]=buffer+the_big_arr[to]
        del the_big_arr[_from][:move]
    
    result=""
    for arr in the_big_arr:
        result+=arr.pop(0)
    
    result.replace("[","").replace("]","")
    
    print("Result")
    print(result.replace("[","").replace("]",""))
    
lines = open("input.txt").read().splitlines()
solution(lines,"1")
solution(lines,"2")