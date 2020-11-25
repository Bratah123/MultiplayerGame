import socket
import pickle


class Network:
    def __init__(self):
        self.server_ip = "192.168.1.157"
        self.server_port = 4444
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.player = self.connect()

    def connect(self):
        try:
            self.socket_client.connect((self.server_ip, self.server_port))
            return pickle.loads(self.socket_client.recv(2048))
        except Exception as e:
            print("[ERROR] Error trying to connect to server", e)

    def send(self, data):
        try:
            self.socket_client.send(pickle.dumps(data))
            return pickle.loads(self.socket_client.recv(2048))
        except Exception as e:
            print("[ERROR] Error trying to send data to server.", e)


