import collections
from collections import Counter


def check(i,t,length,lines):
    sub=""
    if t>length:
            sub=lines[0][i:]
    else:
            sub=lines[0][i:t]
    return sub


def solution(lines,part):

    
    t=4
    if part=="part2":
        t=14
    i=0
    while t<len(lines[0]):
        sub=check(i,t,len(lines[0])-1,lines)
        if len(sub)!=len(set(sub)):
            i=i+1
            t+=1
        else:
            break
    print("Result")
    print(t)


lines = open("input.txt").read().splitlines()
solution(lines,"part1")
solution(lines,"part2")