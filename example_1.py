#!/usr/bin/python
import getpass
from netmiko import Netmiko
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException

host = '192.168.1.11'
username = input('please enter the username: ')
pw = getpass.getpass(prompt='please enter password ')


device = {'ip':host, 'username':username, 'password':pw, 'device_type':'cisco_wlc', 'banner_timeout':8}

try:
	netconnect = Netmiko(**device)
except (NetMikoAuthenticationException, NetMikoTimeoutException):
    print('Failed to connect to {}'.format(host))
    exit()

output = netconnect.send_command('show sysinfo')
print(output)

cmd = ‘show inventory’
output = netconnect.send_command(cmd)
print(output)

cmds = ['show sysinfo','show inventory']
for cmd in cmds:
	output = netconnect.send_command(cmd)
	print(output)
	
netconnect.disconnect()