import threading
import socket

alias = input('Choose an alias >>> ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostbyname(socket.gethostname()), 8000))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'alias':
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print('An error occurred!')
            client.close()
            break

def send():
    while True:
        message = f'{alias}: {input()}'
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()
send_thread = threading.Thread(target=send)
send_thread.start()