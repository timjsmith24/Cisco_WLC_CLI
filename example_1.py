#!/usr/bin/python
import os
import getpass
from netmiko import Netmiko
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException


PATH = os.path.dirname(os.path.abspath(__file__))

os.environ["NET_TEXTFSM"]='{}/ntc-templates/templates/'.format(PATH)


host = '192.168.1.11'
username = input('please enter the username: ')
pw = getpass.getpass(prompt='please enter password ')


device = {'ip':host, 'username':username, 'password':pw, 'device_type':'cisco_wlc', 'banner_timeout':8}

try:
	netconnect = Netmiko(**device)
except (NetMikoAuthenticationException, NetMikoTimeoutException):
    print('Failed to connect to {}'.format(host))
    exit()
'''
output = netconnect.send_command('show sysinfo', use_textfsm=True)
print(output)
'''
cmd = 'show inventory'
output = netconnect.send_command(cmd, use_textfsm=True)
print(output)
'''
cmds = ['show sysinfo','show inventory']
for cmd in cmds:
	output = netconnect.send_command(cmd)
	print(output)
'''	
netconnect.disconnect()