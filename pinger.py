# -*-coding:utf8;-*-
import subprocess
import csv

with open('hosts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ping = subprocess.call(['ping', '-n', '1', row['IP']], stdout=subprocess.DEVNULL)
        #ping = ping.decode(encoding='CP866')
        #if 'bytes=32' in ping or 'байт=32' in ping or '64 bytes' in ping or '64 байта' in ping:
        if ping == 0:
            print('ping ' + row['IP'] + ' is OK!')
        else:
            print('NEOK')
