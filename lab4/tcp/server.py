import socket
import threading


def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024)
        print(f"Клиент: {data.decode()}")


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5555)
server_socket.bind(server_address)
server_socket.listen(5)

print("Ждем соединения...")

client_socket, client_address = server_socket.accept()
print(f"Подключено к {client_address}")

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

while True:
    try:
        message = input()
        client_socket.sendall(message.encode())
    except KeyboardInterrupt:
        print("\nСервер отключен.")
        break

client_socket.close()
server_socket.close()
