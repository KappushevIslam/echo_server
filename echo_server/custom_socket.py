import socket


class CustomSocket(socket.socket):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def send_message(self, message):
        """Отправка сообщения с добавлением заголовка с длиной сообщения."""
        message_bytes = message.encode()
        header = len(message_bytes).to_bytes(4, byteorder='big') # Заголовок с длиной сообщения
        self.sendall(header + message_bytes)

    def receive_message(self):
        """Получение сообщения с учетом заголовка."""
        header = self.recv(4) # Получение заголовка
        if not header:
            return None
        message_length = int.from_bytes(header, byteorder='big') # Преобразование заголовка в длину сообщения
        message = self.recv(message_length) # Получение сообщения
        return message.decode()