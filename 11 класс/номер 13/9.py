from ipaddress import*
ip_y1 = ip_address('118.187.59.255')
ip_y2 = ip_address('118.87.65.115')
for mask in range(32):
    net_1 = ip_network(f'{ip_y1}/{mask}', 0)
    net_2 = ip_network(f'{ip_y2}/{mask}', 0)
    if (net_1 != net_2 and ((net_1[0]) < ip_y1 < net_1[-1]) and (net_2[0]) < ip_y2 < net_2[-1]):
        print(mask)