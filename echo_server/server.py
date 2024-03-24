import socket
import logging
import threading
from custom_socket import CustomSocket

# Настройка логирования
logging.basicConfig(filename='server_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def find_available_port(start_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = start_port
    while True:
        try:
            sock.bind(('', port))
            break
        except socket.error:
            port += 1
    sock.close()
    return port

def handle_client(conn, addr):
    print(f'Подключение клиента: {addr}')
    logging.info(f'Подключение клиента: {addr}')
    while True:
        data = conn.recv(1024)
        if not data:
            print('Отключение клиента...')
            logging.info('Отключение клиента...')
            break
        msg = data.decode()
        if msg == 'exit':
            break
        print('Отправка данных клиенту...')
        logging.info('Отправка данных клиенту...')
        conn.send(data)
    conn.close()


def start_server(port):
    print(f'Запуск сервера на порту {port}...')
    logging.info(f'Запуск сервера на порту {port}...')
    sock = CustomSocket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', port))
    sock.listen(3)
    print('Начало прослушивания порта...')
    logging.info('Начало прослушивания порта...')
    while True:
        conn, addr = sock.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()


if __name__ == "__main__":
    start_port = 9090
    port = find_available_port(start_port)
    start_server(port)
