import socket
import threading
import tkinter


# Функция для отправки сообщений на сервер
def send_message(event=None):
    message = my_message.get()
    my_message.set("")
    client_socket.send(bytes(message, 'utf-8'))


# Функция для получения сообщений от сервера
def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            messages_list.insert(tkinter.END, message)
        except:
            print("Ошибка получения сообщения.")
            break


# Функция для закрытия приложения
def on_closing(event=None):
    my_message.set("{quit}")
    send_message()


# Установка соединения с сервером
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5555))

# Настройка GUI с использованием Tkinter
root = tkinter.Tk()
root.title("Мини-чат")

messages_frame = tkinter.Frame(root)
my_message = tkinter.StringVar()
my_message.set("Введите сообщение")
scrollbar = tkinter.Scrollbar(messages_frame)

messages_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
messages_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
messages_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(root, textvariable=my_message)
entry_field.bind("<Return>", send_message)
entry_field.pack()
send_button = tkinter.Button(root, text="Отправить", command=send_message)
send_button.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)

receive_thread = threading.Thread(target=receive)
receive_thread.start()
tkinter.mainloop()
