#!/usr/bin/env python3
from librip.gens import field


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': None, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'color': 'red'},
    {'title': 'Нечто'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

# Реализация задания 1
def print_list(list):
    for x in range(len(list)):
        print(list[x], end='')
        if x != len(list)-1:
            print(end=', ')

new_items = []
for x in field(goods, 'color1','price'):
    new_items.append(x)
print_list(new_items)
