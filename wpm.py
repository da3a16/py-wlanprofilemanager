import json
from os import popen, system
def enableProfile(intfName, ssid, profile):
    system('netsh interface ip set address name=\"{}\" static {} {} {}'.format(intfName, profile['ip'], profile['mask'], profile['gateway']))
    system('netsh interface ip set dnsserver name=\"{}\" static {} primary validate=no'.format(intfName, profile['dns']))
    if 'dns2' in profile:
        system('netsh interface ip add dns name=\"{}\" addr={} index=2 validate=no'.format(intfName, profile['dns2']))

def enableDHCP(intfName, profile):
    system('netsh interface ip set address name=\"{}\" source=dhcp'.format(intfName))
    if profile == False:
        system('netsh interface ip set dnsserver name=\"{}\" source=dhcp'.format(intfName))
    else:
        system('netsh interface ip set dnsserver name=\"{}\" static {} primary validate=no'.format(intfName, profile['dns']))
        if 'dns2' in profile:
           system('netsh interface ip add dns name=\"{}\" addr={} index=2 validate=no'.format(intfName, profile['dns2']))



system('chcp 437')
stdout = popen('netsh wlan show interfaces').read().split('\n')
for line in stdout:
    if 'Nome' in line or 'Name' in line:
        intfName = line.split(':')[1].strip()
    elif 'SSID' in line and 'BSSID' not in line:
        ssid = line.split(':')[1].strip()

profiles = json.load(open('profiles.config', 'r'))

if ssid in profiles:
    if 'ip' in profiles[ssid] and 'mask' in profiles[ssid] and 'gateway' in profiles[ssid]:
        enableProfile(intfName, ssid, profiles[ssid])
    elif 'dns' in profiles[ssid]:
        enableDHCP(intfName, profiles[ssid])
    else:
        enableDHCP(intfName, False)
else:
    enableDHCP(intfName, False)