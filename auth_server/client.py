import socket


def client_program():
    host = '10.0.2.15'
    port = 9090

    client_socket = socket.socket()
    client_socket.connect((host, port))

    data = client_socket.recv(1024)
    print(data.decode())

    if b'Enter ur name: ' in data:
        name = input("Введите ваше имя: ")
        client_socket.send(name.encode())
        data = client_socket.recv(1024)
        print(data.decode())

        password = input("Введите пароль: ")
        client_socket.send(password.encode())
        data = client_socket.recv(1024)
        print(data.decode())

    client_socket.close()


if __name__ == '__main__':
    client_program()
