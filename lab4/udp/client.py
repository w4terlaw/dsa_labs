import socket

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP и порт сервера, куда будем отправлять данные
server_address = ('localhost', 12345)

# Данные для отправки
message = "Привет, сервер!"

# Отправляем данные
client_socket.sendto(message.encode(), server_address)

# Закрываем сокет
client_socket.close()
