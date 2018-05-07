# python port w/ enhancements by da3a16
forked from https://github.com/xzer/wlanprofilemanager

# Features

Primary & optional secondary DNS setup

Flexible config:
- static IP, static DNS
- IP via DHCP, static DNS
- Full DHCP

# Requirements

- python >= 3.6

# How to use

- clone this repository
- add your own profile to profiles.config
- register a task in task scheduler(control panel->administration tools->task scheduler)
    - set thisrepo/wpm.bat as the operation of the task
    - make sure the task will be executed by user "SYSTEM"
    - define the trigger as following:
        - start at: event
        - basic, log: Microsoft-Windows-WLAN-AutoConfig/Operational
        - source: WLAN-AutoConfig