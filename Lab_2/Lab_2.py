some_input = input('Введите IP-адрес: ')
while len(some_input) > 15:
    if len(some_input) > 15:
        print('Превышено максимально допустимое количество символов (макс. 15 символов)')
    some_input = input('Еще разок: ')
num_list = some_input.split('.')
if len(num_list) != 4:
    print('Неверный формат (Введите 4 октета)')
elif num_list:
    for x in num_list:
        if not x.isdigit():
            print ('Нельзя вводить символы(только числа)')
            break
        elif int(x) < 0 or int(x) > 255:    
            print ('Неверный формат (только числа в диапазоне от 0 до 255)')
            break
i = 0
a = 0
for x in num_list:
    if int(x) == 255:
        i += 1 
    elif int(x) == 0:
        a += 1
if int(num_list[0]) > 0 and int(num_list[0]) < 223:
    print('unicast')
elif int(num_list[0]) > 224 and int(num_list[0]) < 239:
    print('multicast')
elif i == 4:
    print('local broadcast')
elif a == 4:
    print('unassigned')
else:
    print('unused')

#################################################################################


mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []
for elem in mac:
    splitted_elem = elem.split(':')
    splitted_elem = '.'.join(splitted_elem)
    mac_cisco.append(splitted_elem)
print(mac_cisco)

mac_1 = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco_1 = []
[mac_cisco_1.insert(x, mac_1[x].replace(':','.')) for x in range(len(mac_1))]
print(mac_cisco_1)

#################################################################################
access_template = ['switchport mode access',
                   'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan']

fast_int = {'access':{'0/12':'10','0/14':'11','0/16':'17','0/17':'150'},
            'trunk':{'0/1':['add','10','20'],
                     '0/2':['only','11','30'],
                     '0/4':['del','17']} }

for intf, vlan in fast_int['trunk'].items():
    print('interface FastEthernet' + intf)
    for command in trunk_template:
        if command.endswith('allowed vlan'):
            if vlan[0] == 'add':
                print(' {} {} {}'.format(command, vlan[0], str(vlan[1:]).strip('[]').replace('\'','')))
            elif vlan[0] == 'del':
                print(' {} {} {}'.format(command, 'remove', str(vlan[1:]).strip('[]').replace('\'','')))
            elif vlan[0] == 'only':
                print(' {} {}'.format(command, str(vlan[1:]).strip('[]').replace('\'','')))
        else:
            print(' {}'.format(command))   