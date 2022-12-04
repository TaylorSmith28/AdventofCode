"""
File to solve the third day of adventofcode 2022
"""

with open('input.txt', encoding='utf-8') as f:
    lines = f.readlines()

total = 0
total2 = 0

#Solution 1
for line in lines:
    line1, line2 = line.split(',')
    line11, line12 = line1.split('-')
    line21, line22 = line2.split('-')
    #Solution 1
    if (int(line11) <= int(line21)) and (int(line12) >= int(line22)):
        total+=1
    elif (int(line21) <= int(line11)) and (int(line22) >= int(line12)):
        total+=1
    #Solution 2
    if (int(line12) >= int(line21)) and (int(line12) <= int(line22)):
        total2+=1
    elif (int(line11) >= int(line21)) and (int(line11) <= int(line22)):
        total2+=1
    elif(int(line21) >= int(line11)) and (int(line21) <= int(line12)):
        total2+=1
    elif (int(line22) >= int(line11)) and (int(line22) <= int(line12)):
        total2+=1

print(total)
print(total2)