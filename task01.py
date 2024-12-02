#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task01a: 63545
# task01b: 63876
# task01c: 63891



import json

watermelon = "task01a.txt"
banana = "task01b.txt"
pineapple = "task01c.txt"

file =  open(watermelon, 'r')
data = json.load(file) 
largest_number = max(data)
print("==================================================")
print(f"The largest number in file 1 is: {largest_number}")
print("==================================================")

file2 = open(banana,'r')
data2 = json.load(file2)
largest_number2 = max(data2)
print("==================================================")
print(f"the largest number in file 2 is: {largest_number2}")
print("==================================================")

file3 = open(pineapple,'r')
data3 = json.load(file3)
largest_number3 = max(data3)
print("==================================================")
print(f"the largest number in file 3 is: {largest_number3}")
print("==================================================")