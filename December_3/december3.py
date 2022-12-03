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
counter = 0
flag = False
#Solution to part 1
while counter < len(lines):
    first_half_and_second_half = split_list_in_half(lines[counter])
    counter2 = 0
    while counter2 < len(first_half_and_second_half[0]):
        counter3 = 0
        while counter3 < len(first_half_and_second_half[1]):
            if first_half_and_second_half[0][counter2] == first_half_and_second_half[1][counter3]:
                if (first_half_and_second_half[0][counter2]).islower():
                    solution1 += ord(first_half_and_second_half[0][counter2])-96
                    flag = True
                    break
                elif ((first_half_and_second_half[0][counter2]).isupper()):
                    solution1 += ord(first_half_and_second_half[0][counter2])-38
                    flag = True
                    break
            counter3+=1
        counter2+=1
        if(flag):
            flag = False
            break
    counter+=1

#Solution to part 2
counter1 = 0
while counter1 < len(lines):
    counter2 = 0
    while counter2 < len(lines[counter1]):
        counter3 = 0
        while counter3 < len(lines[counter1+1]):
            counter4 = 0
            while counter4 < len(lines[counter1 +2]):
                if(lines[counter1][counter2] == lines[counter1+1][counter3] and lines[counter1+1][counter3]==lines[counter1+2][counter4]):
                    if(lines[counter1][counter2].islower()):
                        solution2 += ord(lines[counter1][counter2])-96
                        flag = True
                        break
                    elif(lines[counter1][counter2].isupper()):
                        solution2 += ord(lines[counter1][counter2])-38
                        flag = True
                        break
                counter4+=1
            counter3 +=1
            if(flag):
                break
        counter2 += 1
        if(flag):
            flag = False
            break
    counter1 +=3

print("Solution 1: " + str(solution1))
print("Solution 2: " + str(solution2))
