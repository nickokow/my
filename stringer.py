# -*-coding:utf8;-*-
import socket
import subprocess
import csv
#Easy function for read csv
with open('hosts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
#Function for checking host availability 
        ping = subprocess.Popen(['ping', '-n', '1',row['IP']], stdout = subprocess.PIPE).communicate()[0]
        ping = ping.decode(encoding='CP866')
        if 'bytes=32' in ping or 'байт=32' in ping or '64 bytes' in ping or '64 байта' in ping:
            print('ping ' + row['IP'] + ' is OK!')
        else:
            print('NEOK')
answer = input('Want a checking port from number? Y or N: ')
if answer == 'Y' or answer == 'y' or answer == 'Д' or answer == 'д':
#function for checking port availability    
    DEFAULT_TIMEOUT = 0.5
    SUCCESS = 0
    with open('hosts.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        port = input('Port here: ')
        for row in reader:
            def check_port(*host_port, timeout=DEFAULT_TIMEOUT):
                sock = socket.socket()
                sock.settimeout(timeout)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                connected = sock.connect_ex(host_port) is SUCCESS
                sock.close()
                return connected
            con = check_port(row['IP'], int(port))
            if con == True:
                print('Port ' + row['IP'] + ': ' + port + ' is OK!')
            else:
                print('Port ' + row['IP'] + ': ' + port + ' is NE OK!')
else:
    print('Nu i otvali koshzanyi meshok')
