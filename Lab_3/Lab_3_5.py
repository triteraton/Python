def generate_access_config(access):
    dictionary = {}
    psecurity = bool(input('Введите True или False: '))
    access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']
    
    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']
    
    for intf, vlan in access.items():
        lst = []
        for comm in port_security:
            if psecurity == 'True':
                lst.append('{}'.format(comm))
            else:
                pass
        for command in access_template:
            if command.endswith('access vlan'):
                lst.append('{} {}'.format(command, vlan))
            else:
                lst.append('{}'.format(command))
        dictionary.update({'interface'+ intf : str(lst) + '\n'})
    return dictionary

access = {'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17,
          'FastEthernet0/17':150 }

[print('{0}: {1}'.format(key, value)) for key, value in generate_access_config(access).items()]


