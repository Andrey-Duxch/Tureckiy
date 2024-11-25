from ipaddress import*
ip_y1 = '154.63.206.129'
ip_y2 = '154.63.100.75'
k = 0
for mask in range(33):
    net1 = ip_network(f'{ip_y1}/{mask}', 0)
    net2 = ip_network(f'{ip_y2}/{mask}', 0)
    if net1 == net2:
        print(net2)
    for ip in net1:
        ip_s = '.'.join(f'{int(x):>08b}' for x in str(ip).split('.'))
        if ip_s.count('1') % 2 == 0:
            k += 1
print(k)