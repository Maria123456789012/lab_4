#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['a', 'b', 'A','D', 'A', 'b']
data4 = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D', 'a', 'a', 'a', 'a', 'b', 'B', 'B']

# Реализация задания 2
uni = Unique(data4, ignore_case = True)
for i in uni:
    pass
print(uni.items)