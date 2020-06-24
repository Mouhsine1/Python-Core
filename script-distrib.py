from netmiko import ConnectHandler

core1 = { 'device_type': 'cisco_ios', 'ip':'192.168.1.120', 'username': 'mouhsine', 'password':'axians'}
core2 = { 'device_type': 'cisco_ios', 'ip':'192.168.1.121', 'username': 'mouhsine', 'password':'axians'}


with open('core1') as s1:
	lines = s1.read().splitlines()
print(lines)
net_connect= ConnectHandler(**core1)
output = net_connect.send_config_set(lines)
print(output)
with open('core2') as s2:
	lines = s2.read().splitlines()
print(lines)
net_connect= ConnectHandler(**core2)
output = net_connect.send_config_set(lines)
print(output)

