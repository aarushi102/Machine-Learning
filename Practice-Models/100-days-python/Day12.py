a =45
b=88
print("A") if a>b else print("=") if a==b else print("B")


fruits = ["Apple","Bananana","Mango","Kiwi","Pear"]

for fruit, index in enumerate(fruits):
    print(index, fruit)

marks = [21,23,45,77,89,44,6,6,786,56]

for i, mark in enumerate(marks,start=2):
    print(mark, i)


## pip freeze --------command to check all the packages need for the project 

## pip freeze > requirements.txt

## pip install -r requirements.txt

import math

print(dir(math))