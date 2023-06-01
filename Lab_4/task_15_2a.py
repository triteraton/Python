# -*- coding: utf-8 -*-
'''
Задание 15.2a

Создать функцию convert_to_dict, которая ожидает два аргумента:
* список с названиями полей
* список кортежей со значениями

Функция возвращает результат в виде списка словарей, где ключи - взяты из первого списка,
а значения подставлены из второго.

Например, если функции передать как аргументы список headers и список
[('FastEthernet0/0', 'up', 'up', '10.0.1.1'),
 'FastEthernet0/1', 'up', 'up', '10.0.2.1')]

Функция должна вернуть такой список со словарями (порядок полей может быть другой):
[{'interface': 'FastEthernet0/0', 'status': 'up', 'protocol': 'up', 'address': '10.0.1.1'},
 {'interface': 'FastEthernet0/1', 'status': 'up', 'protocol': 'up', 'address': '10.0.2.1'}]

Проверить работу функции:
* первый аргумент - список headers
* второй аргумент - результат, который возвращает функция parse_sh_ip_int_br из задания 15.2, если ей как аргумент передать sh_ip_int_br.txt.


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import re

def parse_sh_ip_int_br(file_name):
    with open(file_name, 'r') as f:
        output = f.read()
    pattern = re.compile(r'(\S+)\s+([\d.]+|unassigned)\s+\S+\s+\S+\s+(\S+)\s+(\S+)')
    matches = re.findall(pattern, output)
    result = [(m[0], m[1], m[2], m[3]) for m in matches]
    return result

def convert_to_dict(headers, values):
    # Create a list of dictionaries with the field names and values
    result = [dict(zip(headers, v)) for v in values]

    return result

# Define the headers
headers = ['interface', 'address', 'status', 'protocol']

# Call the parse_sh_ip_int_br function to get the list of tuples with values
values = parse_sh_ip_int_br('sh_ip_int_br.txt')

# Call the convert_to_dict function to convert the list of tuplesto a list of dictionaries
result = convert_to_dict(headers, values)
print(result)