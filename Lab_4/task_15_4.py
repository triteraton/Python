# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
'''
import re

def get_ints_without_description(config_file):
    # Read the configuration file
    with open(config_file, 'r') as f:
        config = f.readlines()

    # Process the configuration to find interfaces without description
    intfs_without_desc = []
    intf_name = ''
    intf_has_desc = False
    for line in config:
        if line.startswith('interface'):
            if intf_has_desc == False and intf_name != '':
                intfs_without_desc.append(intf_name)
            intf_name = line.split()[1]
            intf_has_desc = False
        elif line.startswith(' description'):
            intf_has_desc = True
        elif line.startswith('!'):
            if intf_has_desc == False and intf_name != '':
                intfs_without_desc.append(intf_name)
            intf_has_desc = False

    return intfs_without_desc

config_file = 'config_r1.txt'
intfs_without_desc = get_ints_without_description(config_file)
print(intfs_without_desc)
