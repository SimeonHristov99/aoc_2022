def part_one(lines):
    counter=0
    for pair in lines:
        elfs=pair.split(",")
        elf1 = list(map(int, elfs[0].split("-")))
        elf2=list(map(int, elfs[1].split("-")))
        if (elf1[0]<=elf2[0] and elf1[1]>=elf2[1]) or  (elf1[0]>=elf2[0] and elf1[1]<=elf2[1]):
            counter+=1
    print(counter)

def part_two(lines):
    counter=0
    for pair in lines:
        elfs=pair.split(",")
        elf1 = list(map(int, elfs[0].split("-")))
        elf2=list(map(int, elfs[1].split("-")))
    
        if (elf1[0]<=elf2[0] and elf1[1]>=elf2[0]) or (elf2[0]<=elf1[0] and elf2[1]>=elf1[0]):
            counter+=1

    print(counter)
            
            
lines = open("input.txt").read().splitlines()
part_one(lines)
part_two(lines)