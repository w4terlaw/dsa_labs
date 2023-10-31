import socket

# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP и порт, на котором сервер будет принимать данные
server_address = ('localhost', 12345)
server_socket.bind(server_address)

print("Ждем данные...")

# Принимаем данные и информацию об отправителе
data, address = server_socket.recvfrom(1024)
print(f"Получено от {address}: {data.decode()}")

# Закрываем сокет
server_socket.close()