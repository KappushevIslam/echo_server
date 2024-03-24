import socket

def get_input(prompt, default):
    user_input = input(prompt)
    return user_input if user_input else default

def client_program():
    host = get_input("Введите имя хоста (по умолчанию '10.0.2.15'): ", '10.0.2.15')
    port = int(get_input("Введите номер порта (по умолчанию 9090): ", '9090'))

    sock = socket.socket()
    sock.setblocking(1)
    sock.connect((host, port))

    while True:
        msg = input("Введите сообщение (или 'exit' для выхода): ")
        if msg == 'exit':
            break
        sock.send(msg.encode())

        data = sock.recv(1024)
        print(data.decode())

    sock.close()

if __name__ == '__main__':
    client_program()