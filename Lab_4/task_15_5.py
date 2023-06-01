# -*- coding: utf-8 -*-
'''
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.
Функция должна обрабатывать вывод команды show cdp neighbors и генерировать на основании вывода команды описание для интерфейсов.
Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1
Функция должна возвращать словарь, в котором ключи - имена интерфейсов, а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'
Проверить работу функции на файле sh_cdp_n_sw1.txt.
'''
import re

def generate_description_from_cdp(filename):
    with open(filename) as f:
        output = f.read()
    
    descriptions = {}
    for line in output.split('\n'):
        if 'Eth' in line:
            fields = line.split()
            interface = fields[1]  # e.g. "Eth 0/0"
            neighbor = fields[2]  # e.g. "R1"
            descriptions[interface] = f"description Connected to {neighbor} port {interface}"
    
    return descriptions

descriptions = generate_description_from_cdp('sh_cdp_n_sw1.txt')
print(descriptions)