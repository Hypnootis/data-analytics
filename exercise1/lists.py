import numpy

ones_list = []
sevens_list = []
numbers_list = []
evens_list = []
years_list = []

for i in range(15):
    ones_list.append(1)
    sevens_list.append(7)

for i in range(100, 151):
    numbers_list.append(i)

for i in range(1, 101):
    if i % 2 == 0:  
        evens_list.append(i)
        
for i in range(1950, 2021):
    if i % 4 == 0:
        years_list.append(i)