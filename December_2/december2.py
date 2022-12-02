"""
File to solve the first day of adventofcode 2022
"""

with open('input.txt', encoding='utf-8') as f:
    lines = f.readlines()

first_total_points = 0
second_total_points = 0

for i in lines:
    #First Solution
    first_total_points +=1
    if (i[0] == 'A' and i[2] == 'Y') | (i[0] == 'B' and i[2] == 'Z') | (i[0] == 'C' and i[2] == 'X'):
        first_total_points += 6
    elif (i[0] == 'A' and i[2] == 'X') | (i[0] == 'B' and i[2] == 'Y') | (i[0] == 'C' and i[2] == 'Z'):
        first_total_points += 3
    if i[2] == 'Z':
        first_total_points += 2
    elif i[2] == 'Y':
        first_total_points += 1
    #Second Solution
    second_total_points +=1
    if i[2] == 'Z':
        second_total_points += 6
        if i[0] == 'A':
            second_total_points +=1
        elif i[0] == 'B':
            second_total_points +=2
    elif i[2]== 'Y':
        second_total_points += 3
        if i[0] == 'C':
            second_total_points +=2
        elif i[0] == 'B':
            second_total_points +=1
    else:
        if i[0] == 'A':
            second_total_points +=2
        elif i[0] == 'C':
            second_total_points +=1

print("First Solution: " +str(first_total_points))
print("Second Solution: " +str(second_total_points))
