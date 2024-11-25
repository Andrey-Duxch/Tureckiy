from ipaddress import*
k = 0
mask = '255.255.255.192'
for A in range(256):
    ip_y = ip_address(f'207.0.{A}.167')
    net = ip_network(f'{ip_y}/{mask}', 0)
    if all(f'{ip:b}'[:16].count('0') > f'{ip:b}'[16:].count('0') for ip in net) and net[0] < ip_y < net[-1]:
        k+=1
print(k)

