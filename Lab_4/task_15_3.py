# -*- coding: utf-8 -*-
'''
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
'''
import re

def convert_ios_nat_to_asa(input_file, output_file):
    # Read the input file
    with open(input_file, 'r') as f:
        ios_nat_config = f.readlines()

    # Process the NAT rules
    asa_nat_config = []
    for rule in ios_nat_config:
        # Parse the IOS NAT rule
        tokens = rule.strip().split()
        ip_address = tokens[3]
        port = tokens[4]
        interface = tokens[6]
        mapped_port = tokens[7]

        # Create the ASA NAT rule
        asa_rule = f"object network LOCAL_{ip_address}\n" \
                   f" host {ip_address}\n" \
                   f" nat (inside,outside) static interface service tcp {port} {mapped_port}"
        asa_nat_config.append(asa_rule)

    # Write the ASA NAT rules to the output file
    with open(output_file, 'w') as f:
        f.write('\n'.join(asa_nat_config))
    return

input_file = 'cisco_nat_config.txt'
output_file = 'asa_nat_config.txt'
convert_ios_nat_to_asa(input_file, output_file)