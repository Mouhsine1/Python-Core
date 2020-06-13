from netmiko import ConnectHandler

dist1 = { 'device_type': 'cisco_ios', 'ip':'192.168.1.120', 'username': 'mouhsine', 'password':'axians'}
dist2 = { 'device_type': 'cisco_ios', 'ip':'192.168.1.121', 'username': 'mouhsine', 'password':'axians'}
dist3 = { 'device_type': 'cisco_ios', 'ip':'192.168.1.122', 'username': 'mouhsine', 'password':'axians'}
dist4 = { 'device_type': 'cisco_ios', 'ip':'192.168.1.123', 'username': 'mouhsine', 'password':'axians'}


with open('distrib1') as s1:
	lines = s1.read().splitlines()
print(lines)
net_connect= ConnectHandler(**dist1)
output = net_connect.send_config_set(lines)
print(output)
with open('distrib2') as s2:
	lines = s2.read().splitlines()
print(lines)
net_connect= ConnectHandler(**dist2)
output = net_connect.send_config_set(lines)
print(output)
with open('distrib3') as s3:
	lines = s3.read().splitlines()
print(lines)
net_connect= ConnectHandler(**dist3)
output = net_connect.send_config_set(lines)
print(output)
with open('distrib4') as s4:
	lines = s4.read().splitlines()
print(lines)
net_connect= ConnectHandler(**dist4)
output = net_connect.send_config_set(lines)
print(output)

