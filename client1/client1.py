import os
import re
import time
import socket
import http.client
import urllib.parse

print('Client is running...')

while True:
    print('Welcome to our Distributed HTTP Calculator')
    #exp = input('Enter an expression: ')
    try:
        connection = http.client.HTTPConnection('localhost', 8080)
        connection.request('GET', '/ping')
    except ConnectionRefusedError:
        os.system('clear')
        print('Server is not running. Press enter to exit.')
        time.sleep(2)
        continue
    exp = input('Enter an expression (q to quit): ')
    if exp == 'q':
        break
    query = urllib.parse.quote(exp)
    try:
        connection = http.client.HTTPConnection('localhost', 8080)
        connection.request('GET', f'/?exp={query}')
        response = connection.getresponse()
        result = response.read().decode('utf-8')
        print('\nResult:', result)
    except ConnectionRefusedError:
        os.system('clear')
        print('Server is not running. Press enter to exit.')
        time.sleep(2)
        continue