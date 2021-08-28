import os
import time
import socket
import http.client

print('Client is running...')

while True:
    os.system('clear')
    print('Welcome to our Distributed HTTP Calculator')
    print('Please enter a operation you want to perform')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Evaluate expression')
    print('6. Exit')
    choice = input('Enter your choice: ')