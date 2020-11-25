import socket
from threading import Thread
import pickle
import random
from player import Player

players = {}


class Server:

    def __init__(self):
        self.server_ip = "192.168.1.157"
        self.port = 4444
        self.server_settings = (self.server_ip, self.port)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.player_index = 0

    def start(self):
        try:
            self.server_socket.bind(self.server_settings)
        except Exception as e:
            print("[ERROR] Error trying to bind server.", e)

        self.server_socket.listen(10)
        self.listen_connections()
        print(f"[CONNECTION] Listening for connections on {self.port}")

    def listen_connections(self):
        while True:
            conn, addr = self.server_socket.accept()
            print(f"[CONNECTION] Connection from {addr}")
            ACCEPT_THREAD = Thread(target=self.thread_client, args=(conn, addr, self.player_index))
            ACCEPT_THREAD.start()
            self.player_index += 1

    def thread_client(self, conn, addr, player_index):
        rand_x = random.randrange(1, 50)
        rand_y = random.randrange(1, 50)
        color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

        player = Player(rand_x, rand_y, 50, 50, color)
        players[player_index] = player
        conn.send(pickle.dumps(players[player_index]))
        print("[SERVER] Started thread with player index:", player_index)
        current_player = players[player_index]
        is_online = True
        while is_online:
            try:
                data = pickle.loads(conn.recv(2048))
                players[player_index] = data
                list_players = {}
                if not data:
                    print(f"{addr} has disconnected")
                    is_online = False
                else:
                    for player_idx in players:
                        player = players[player_idx]
                        if player != current_player:
                            list_players[player_idx] = player

                conn.sendall(pickle.dumps(list_players))

            except Exception as e:
                print(f"[SERVER] {addr} has disconnected.", e)
                is_online = False

        print(f"[SERVER] Ended threaded tasks for client: {addr}")
        self.player_index -= 1
        del players[player_index]
        conn.close()


def main():
    server = Server()
    server.start()


if __name__ == '__main__':
    main()
