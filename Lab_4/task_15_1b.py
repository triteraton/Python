# -*- coding: utf-8 -*-
'''
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким образом, чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''

import re

def get_ip_from_cfg(filename):
    result = {}
    with open(filename) as f:
        cfg = f.read()
        regex = re.compile(r"interface (\S+)\n.*?ip address (\S+) (\S+)(.*?ip address (\S+) (\S+))?", re.DOTALL)
        matches = regex.finditer(cfg)
        for match in matches:
            interface = match.group(1)
            ip_address1 = match.group(2)
            mask1 = match.group(3)
            ip_address2 = match.group(5)
            mask2 = match.group(6)
            if ip_address2:
                result[interface] = [(ip_address1, mask1), (ip_address2, mask2)]
            else:
                result[interface] =[(ip_address1, mask1)]
    return result

result = get_ip_from_cfg('config_r2.txt')
print(result)