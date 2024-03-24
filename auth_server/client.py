import socket
import threading


def receive_messages(client):
    while True:
        message = client.recv(1024)
        if message:
            print(message.decode('utf-8'))
        else:
            break


def client_program():
    host = '10.0.2.15'
    port = 9090

    client_socket = socket.socket()
    client_socket.connect((host, port))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input("Введите сообщение: ")
        client_socket.send(message.encode('utf-8'))
        if message.lower() == 'bye':
            break

    client_socket.close()


if __name__ == '__main__':
    client_program()
