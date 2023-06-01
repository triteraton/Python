# -*- coding: utf-8 -*-
'''
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

'''
import re

def parse_sh_ip_int_br(file_name):
    with open(file_name, 'r') as f:
        output = f.read()
    pattern = re.compile(r'(\S+)\s+([\d.]+|unassigned)\s+\S+\s+\S+\s+(\S+)\s+(\S+)')
    matches = re.findall(pattern, output)
    result = [(m[0], m[1], m[2], m[3]) for m in matches]
    return result

result = parse_sh_ip_int_br('sh_ip_int_br.txt')
print(result)