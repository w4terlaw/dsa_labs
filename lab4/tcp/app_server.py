import socket
import threading

# Список для хранения подключенных клиентов
clients = []


# Функция для обработки сообщений от клиентов
def handle_client(client_socket, nickname):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            broadcast(message, nickname)
        except:
            index = clients.index(client_socket)
            clients.remove(client_socket)
            client_socket.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} покинул чат!', '')
            nicknames.remove(nickname)
            break


# Функция для рассылки сообщений всем клиентам
def broadcast(message, sender):
    for client in clients:
        client.send(bytes(sender + ": " + message, 'utf-8'))


# Запуск сервера
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen()

    while True:
        try:
            client_socket, addr = server.accept()
            client_socket.send('Введите имя пользователя\n'.encode('utf-8'))
            nickname = client_socket.recv(1024).decode('utf-8')
            nicknames.append(nickname)
            clients.append(client_socket)

            print(f"Подключился новый клиент: {nickname}")
            broadcast(f'{nickname} присоединился к чату!', '')
            client_socket.send('Подключено к серверу'.encode('utf-8'))

            thread = threading.Thread(target=handle_client, args=(client_socket, nickname))
            thread.start()
        except:
            ...

# Запуск сервера
nicknames = []


def main():
    print('Сервер запущен...')
    start_server()


if __name__ == '__main__':
    main()
