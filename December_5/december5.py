import re
import copy

with open('input.txt', encoding='utf-8') as f:
    lines = f.readlines()

stack1 = [['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G'],
['S', 'W', 'C'],
['R' ,'Z', 'T', 'M'],
['D', 'T', 'C', 'H', 'S', 'P', 'V'],
['G', 'P', 'T', 'L', 'D' , 'Z'],
['F','B','R','Z','J','Q','C','D'],
['S','B','D','J','M','F','T','R'],
['L','H','R','B','T','V','M'],
['Q','P','D','S','V']]

stack2 = copy.deepcopy(stack1)
solution1 = []
solution2 = []

for  line in lines:
    numbers = re.findall(r'\d+', line)
    mylist = []
    # Solution 1
    for i in range(0, int(numbers[0])):
        stack1[int(numbers[2])-1].append(stack1[int(numbers[1])-1].pop())
    # Solution 2 
    for i in range(0, int(numbers[0])):    
        mylist.append(stack2[int(numbers[1])-1].pop())
    for i in range(0, int(numbers[0])):
        stack2[int(numbers[2])-1].append(mylist.pop())

for i in range(0,9):
     solution1.append(stack1[i].pop())
     solution2.append(stack2[i].pop())

print("Solution 1: "+str(solution1))
print("Solution 2: "+str(solution2))
