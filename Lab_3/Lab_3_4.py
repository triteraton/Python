def get_int_vlan_map(file):
    with open(file, 'r') as f:
        access_dict = {}
        trunk_dict  = {}
        data = f.read()
        splitted_data = data.split('!')
        lst_access = []
        for elem in splitted_data:
            if 'interface' and 'mode access' in elem:
                stripped = elem.strip()
                lst_access.append(stripped)
        print(lst_access)
        for part in lst_access:
            part.split("\n")
        print(lst_access)
       # for x in lst_of_parts: 
       #     access_dict.update({x[0][10:] : x[2][24:]})
        
        print(access_dict)
        print(trunk_dict)
       
        
    return access_dict, trunk_dict

get_int_vlan_map('config_sw1.txt')
    