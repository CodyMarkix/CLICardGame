#!/usr/bin/env python3
import socket
import threading

# All-caps variables are constants. (JS equivalent is "const <varname> = ...")
HEADER = 64 # Could become too small, raise in case
PORT = 5000
SERVER = socket.gethostbyname(socket.gethostname()) # Automatically get the host's IP address
ADDR = (SERVER, PORT)
FORMAT = 'utf-8' # The format to decode incoming sockets with
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False # could also be "break", both are possible
            
            print(f"[{addr}] {msg}")
            conn.send("Msg recieved".encode(FORMAT))

def start():
    print("[OK] Server started!")
    print("[OK] Listening at ip "+ str(SERVER) +".")
    print("[OK] Listening at port "+ str(PORT) +".")
    server.listen()
    while True:
        conn, addr = server.accept()
        handlethread = threading.Thread(target=handle_client, args=(conn, addr))
        handlethread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] Server is starting...")
start()