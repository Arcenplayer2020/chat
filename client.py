import socket
import threading
ip = input("ip? : ")
nickname = input('choose a nickname')
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((ip,879))

def recieve():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print('error')
            client.close()
            break
def write():
    while True :
        message = f'{nickname} : {input("")}'
        client.send(message.encode('utf-8'))

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()



