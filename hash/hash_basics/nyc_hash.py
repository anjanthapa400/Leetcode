# This problem includes the hash problem on the basics of nyc csv file

import csv 
import random
import re

file = open('nyc_weather.csv')
csvreader = csv.reader(file)
header = []
row = []
header = next(csvreader)
for x in csvreader:
    row.append(x)

random.shuffle(row)

# Half an hour on the concepts of strings

dict = {}
l = []
regex = "\d+"
for i in row:
    l = re.findall(regex,i[0])
    dict[int(l[0])] = i

print(dict)

# To be continued on feb 16
# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/4_HashTable_2_Collisions/4_hash_table_exercise.md




