import threading
import requests
import customfuncs
import socket
import mainmenu

class Game:
    def play():
        print("hello world!")

    def join():
        # requests.get(mainmenu.joinip)
        Client()

class Client():
    HEADER = 64 # Could become too small, raise in case
    PORT = 5000
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"
    SERVER = "192.168.0.108"
    ADDR = (SERVER, PORT)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def __init__(self):

        Client.send("HI!")
        input()
        Client.send("Hello")
        input()
        Client.send(Client.DISCONNECT_MESSAGE)
        print(Client.client.recv(1024).decode(Client.FORMAT))

    def connect():
        Client.client.connect(Client.ADDR)
    
    def send(msg):
        message = msg.encode(Client.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(Client.FORMAT)
        send_length += b' ' * (Client.HEADER - len(send_length))
        Client.client.send(send_length)
        Client.client.send(message)
