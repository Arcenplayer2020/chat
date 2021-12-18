import socket
import threading

server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1],879))
print(f'сервер запущен на ip {socket.gethostbyname_ex(socket.gethostname())[-1][-1]}')
server.listen()
clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('utf-8'))
            nicknames.remove(nickname)
            break
def receive():
    while True:
        client,adress = server.accept()
        print('client connected')
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)
        broadcast(f'{nickname} joined the chat'.encode('utf-8'))
        thread = threading.Thread(target=handle,args=(client,))
        thread.start()

print('serveer is listenung')
receive()
