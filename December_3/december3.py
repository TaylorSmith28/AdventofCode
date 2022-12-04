"""
File to solve the third day of adventofcode 2022
"""

with open('input.txt', encoding='utf-8') as f:
    lines = f.readlines()

def split_list_in_half(lst):
    middle = len(lst) // 2
    return [lst[:middle],lst[middle:]]

solution1 = 0
solution2 = 0
#Solution to part 1
for line in lines:
    first_half_and_second_half = split_list_in_half(line)
    counter2 = 0
    while counter2 < len(first_half_and_second_half[0]):
        if first_half_and_second_half[0][counter2] in first_half_and_second_half[1]:
            if (first_half_and_second_half[0][counter2]).islower():
                solution1 += ord(line[counter2])-96
            elif (first_half_and_second_half[0][counter2]).isupper():
                solution1 += ord(line[counter2])-38
            break
        counter2+=1

#Solution to part 2
counter = 0
while counter < len(lines):
    counter2 = 0
    while counter2 < len(lines[counter]):
        if (lines[counter][counter2] in lines[counter+1]) and (lines[counter][counter2] in lines[counter+2]):
            if (lines[counter][counter2]).islower():
                solution2 += ord(lines[counter][counter2])-96
            elif ((lines[counter][counter2]).isupper()):
                solution2 += ord(lines[counter][counter2])-38
            break
        counter2+=1
    counter+=3

print("Solution 1: " + str(solution1))
print("Solution 2: " + str(solution2))
