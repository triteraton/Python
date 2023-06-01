##Exercise
print('\nexercise_3_1\n')
##_3_1

NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print (NAT.replace("Fast", "Gigabit"))

##Exercise
print('\nexercise_3_2\n')
##_3_2

MAC = 'AAAA:BBBB:CCCC'
print ('.'.join(MAC.split(':')))

##Exercise
print('\nexercise_3_3\n')
##_3_3

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
print (CONFIG.split()[-1].split(','))

##Exercise
print('\nexercise_3_4\n')
##_3_4

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

ListCom = (list(set(command1.split()[-1].split(',')).intersection(set(command2.split()[-1].split(',')))))
list(map(int, ListCom)).sort()
print (list(map(int, ListCom)))

##Exercise
print('\nexercise_3_5\n')
##_3_5

VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]

##newList = list((set(VLANS)))
##newList.sort()
print (sorted(list((set(VLANS)))))

##Exercise
print('\nexercise_3_6\n')
##_3_6

ospf_route = 'OSPF 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
"""
keys = ['Protocol:', 'Prefix:', 'AD/Metric', 'Next-Hop:', 'Last update:', 'Outbound Interface:']
values = ospf_route.replace(',', '').replace('via','').replace('[','').replace(']','').split()

output = list(dict(zip(keys, values)).items())
a = str(list(output[0])).strip('[]') + str(list(output[1])).strip('[]') + str(list(output[2])).strip('[]') + str(list(output[3])).strip('[]') + str(list(output[4])).strip('[]') + str(list(output[5])).strip('[]')
b= a.replace(',',' ').replace('\'',' ').split()
c = '\n'.join(b[0::2])
print (c)
"""

s = ospf_route.split()
#print(s)
s_protocol = s[0]
s_prefix  = s[1]
s_metric = s[2]
s_metric = s_metric[1:-1]
s_next_hop = s[4]
s_next_hop = s_next_hop[:-1]
s_last_upd = s[5]
s_last_upd = s_last_upd[:-1]
s_interface = s[6]

print ("Protocol:",'{:>25}'.format(s_protocol))
print ('Prefix:','{:>35}'.format(s_prefix))
print ('AD/Metric:','{:>26}'.format(s_metric))
print ('Next-Hop:','{:>30}'.format(s_next_hop))
print ('Last update:','{:>23}'.format(s_last_upd))
print ('Outbound Interface:','{:>26}'.format(s_interface ))

##Exercise
print('\nexercise_3_7\n')
##_3_7

MAC = 'AAAA:BBBB:CCCC'

mac = MAC.split(':')
new_mac = "".join(mac)
print(bin(int(new_mac, 16)))

##Exercise
print('\nexercise_3_8\n')
##_3_8

IP = '192.168.3.1'.split('.')
print (IP[0],'{:>8}'.format(IP[1]),'{:>6}'.format(IP[2]),'{:>8}'.format(IP[3]))
binIp = [bin( int(IP[0]) )[2:], bin( int(IP[1]) )[2:], bin( int(IP[2]) )[2:], bin( int(IP[3]) )[2:]]
print (binIp[0].zfill(8), '{:>2}'.format(binIp[1].zfill(8)), '{:>2}'.format(binIp[2].zfill(8)), '{:>2}'.format(binIp[3].zfill(8)))

##Exercise
print('\nexercise_3_9\n')
##_3_9

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

List = num_list
element = 15
print(List)
print ( List.index(element) )