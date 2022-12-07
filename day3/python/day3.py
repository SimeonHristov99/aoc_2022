import numpy as np
def part_one(lines):
 print(lines)

 print(ord("A"))#65 , -38
 print(ord("a")) #97, -96

 total_sum=0
 for line in lines:
    mid=len(line)//2
    first_half=line[0:mid]
    second_half=line[mid:]
    common_element=set([element for element in first_half if element in second_half]).pop()
    if common_element.isupper():
        total_sum+=ord(common_element)-38
    else:
        total_sum += ord(common_element) - 96

 print(total_sum)




def part_two(lines):
 arr=np.array_split(lines,len(lines)//3)
 total_sum=0
 for line in arr:
     common_element = set([element for element in line[0] if element in line[1] and element in line[2]]).pop()
     print(common_element)
     total_sum+= ord(common_element) - 38 if common_element.isupper() else ord(common_element) - 96

 print(total_sum)

lines = open("input.txt").read().splitlines()
part_two(lines)