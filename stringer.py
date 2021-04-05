# -*-coding:utf8;-*-
# qpy:3
# qpy:console

import socket
import os
import platform
import subprocess
import csv
with open('hosts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ping = subprocess.Popen(['ping', '-n', '1',row['IP']], stdout = subprocess.PIPE).communicate()[0]
        ping = ping.decode(encoding='CP866')
        if 'bytes=32' in ping or 'байт=32' in ping or '64 bytes' in ping or '64 байта' in ping:
            print('ping ' + row['IP'] + ' is OK!')
        else:
            print('NEOK')

DEFAULT_TIMEOUT = 0.5
SUCCESS = 0
with open('hosts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        def check_port(*host_port, timeout=DEFAULT_TIMEOUT):
            sock = socket.socket()
            sock.settimeout(timeout)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            connected = sock.connect_ex(host_port) is SUCCESS
            sock.close()
            return connected
        port = input('Port here: ')
        con = check_port(row['IP'], int(port))
        for con in port:
            if con == True:
                print('Port ' + row['IP'] + ': ' + port + ' is OK!')
            else:
                print('Port ' + row['IP'] + ': ' + port + ' is NE OK!')



#----------------------------------------------------------------------------------------------------------------------#
#for result in (ping, con):
#    if 'bytes=32' in ping or 'байт=32' in ping or '64 bytes' in ping or '64 байта' in ping:
#        print('ping ' + host + ' is OK!')
#    if con == True and 'bytes=32' in ping or 'байт=32' in ping or '64 bytes' in ping or '64 байта' in ping:
#        print('Ping {0} And Port {1} is Valid!'.format(host, str(port)))
#        break
#    elif con == False and ping == 0:
#        print('Port ' + str(port) +  ' from ' + host + 'Is not valid')
#        break
#    else:
#        print('Not valid')
#        break