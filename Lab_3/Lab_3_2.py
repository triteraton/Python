def generate_trunk_config(trunk):
    lst = []
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']

    for intf, vlan in trunk.items():
        lst.append(intf)
        for command in trunk_template:
            if command.endswith('allowed vlan'):
                lst.append(' {} {}'.format(command, str(vlan).strip('[]').replace('\'','')))
            else:
                lst.append(' {}'.format(command))   
    
    return lst

trunk = { 'FastEthernet0/1':[10,20,30],
          'FastEthernet0/2':[11,30],
          'FastEthernet0/4':[17] }

[print(f'{elem}') for elem in generate_trunk_config(trunk)]