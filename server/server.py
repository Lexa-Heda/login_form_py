"""
Author: Nico Freitag
"""

import socket, threading, struct, sqlite3
import time
from ssl import Purpose
from saveDataManager import *
from socket import timeout


class Server:
    def __init__(self):
        self.clients = []
        self.queue_lock = threading.Lock()
        self.used_clients = []
        self.threads = []

        self.host = ('localhost', 80)
        self.port = 80
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.host)

        self.conn = sqlite3.connect('data/members.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS members
                                (id INTEGER PRIMARY KEY, username TEXT, password TEXT, email TEXT)
                                ''')
        self.conn.commit()

        self.running = True

    def listen_thread(self, socket):
        while self.running:
            socket.settimeout(1)
            try:
                socket.listen(1)
                client_socket, client_address = socket.accept()
                print("found Client")
                with self.queue_lock:
                    self.clients.append((client_socket, client_address))
                    client_function_thread = threading.Thread(target=self.function_thread, args=[client_socket, ])
                    client_function_thread.start()
                    self.threads.append(client_function_thread)
            except timeout:
                pass  
        print("Listen thread exiting")

    def recive_Data(self, client):
        data = client.recv(1024).decode()
        return data

    def function_thread(self, client):
        print("Works!")
        while True:
            try:
                purpose = self.recive_Data(client)
                print(purpose)
                self.socket.settimeout(9999)
                if purpose == "test":
                    print("Access")
                    response = "Hallo Test"
                    time.sleep(2)
                    self.send_data(response)

                elif purpose == "login":
                    response: str = "ok"
                    self.send_data(response)
                    user_data = self.socket.recv(1024).decode().split(",")
                    response: bool = self.get_member(user_data[0], user_data[1])

                else:
                    print("Purpose not found")
            except timeout:
                break

    def setup_server(self):
        print("setup")
        self.listen_thread = threading.Thread(target=self.listen_thread, args=[self.socket])
        self.threads.append(self.listen_thread)

        for thread in self.threads:
            print("thread start")
            thread.start()
        print("Hi")
        input("Press enter to continue:\n")
        self.shutdwon()

    def shutdwon(self):
        self.running = False
        for client in self.clients:
            client[0].close()

        for thread in self.threads:
            thread.join()
        self.socket.close()

    def send_data(self, data):
        encoded_data = b""
        if isinstance(data, str):
            self.socket.send(data.encode())
        elif isinstance(data, int):
            encoded_data += (struct.pack("i", data))
            self.socket.send(encoded_data)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, str):
                    encoded_data += (item.encode())
                elif isinstance(item, int):
                    encoded_data += struct.pack("i", item)
            self.socket.send(encoded_data)

    def get_member(self, username, password):
        self.cursor.execute("SELECT * FROM members WHERE username=? AND password=?", (username, password))
        member = self.cursor.fetchone()
        if member:
            return True
        else:
            return False

if __name__ == "__main__":
    server = Server()
    server.setup_server()


