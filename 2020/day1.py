import numpy as np
import os
from csv import DictReader

readpath = "C:\\Users\\BAP\\Desktop\\Projects\\Advent of Code\\2020"
file = ""
items = []

os.chdir(readpath)

for currentfile in os.listdir():
    if "day_1_data" in str(currentfile):
        file = np.genfromtxt(currentfile,dtype=int)
        break

#file = np.array([1721,979,366,299,675,1456])
matrix = np.zeros([file.size,file.size])

for element,row in zip(file,range(file.size)):
    matrix[row,:] = file+element

for element in file:
    if element in 2020-matrix:
        items.append(element)

x = 1

for item in items:
    x = x*item

print(x)

print(items)