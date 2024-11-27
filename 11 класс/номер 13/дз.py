from ipaddress import*
ip_s = '148.195.140.0'
ip_y = '148.195.140.28'
for mask in range(33):
    net = ip_network(f'{ip_y}/{mask}',0)
    if ip_s in str(net):
        print(bin(int(net.netmask)))
#наименьшее количество единиц: 22