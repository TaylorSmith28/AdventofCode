"""
File to solve the first day of adventofcode 2022
"""

with open('input.txt', encoding="utf-8") as f:
    lines = f.readlines()

first = 0
second = 0
third = 0
elfs_total_calories = 0
for index in lines:
    try:
        elfs_total_calories += int(index)
    except ValueError:
        if elfs_total_calories > first:
            third = second
            second = first
            first = elfs_total_calories
        elif elfs_total_calories > second:
            third = second
            second = elfs_total_calories
        elif elfs_total_calories > third:
            third = elfs_total_calories
        elfs_total_calories = 0
print(first)
print(first + second + third)
