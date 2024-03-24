import socket
import hashlib
import json


# Функция для генерации хеша пароля
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Функция для проверки пароля
def check_password(stored_password, password):
    return stored_password == hash_password(password)


# Функция для загрузки данных пользователей из файла
def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# Функция для сохранения данных пользователей в файл
def save_users(users):
    # Удаляем объекты socket из словаря перед сохранением
    cleaned_users = {ip: {'name': user['name'], 'password': user['password']} for ip, user in users.items()}
    with open('users.json', 'w') as file:
        json.dump(cleaned_users, file)


# Функция для обработки соединения с клиентом
def handle_client(conn):
    ip = conn.getpeername()[0]
    users = load_users()

    if ip in users:
        conn.send(b'Hello, ' + users[ip]['name'].encode('utf-8'))
    else:
        conn.send(b'Enter ur name: ')
        name = conn.recv(1024).decode().strip()
        conn.send(b'Enter ur password: ')
        password = conn.recv(1024).decode().strip()
        users[ip] = {'name': name, 'password': hash_password(password)}
        save_users(users)
        conn.send(b'Registration successful')


# Основная функция сервера
def server_program():
    host = '10.0.2.15'
    port = 9090

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(3)

    print(f"Сервер запущен на {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Подключение от {addr}")
        handle_client(conn)
        conn.close()


if __name__ == '__main__':
    server_program()
