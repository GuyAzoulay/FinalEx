import sys
import threading
import socket

#
# import socket
#
# # import threading library
# import threading
#
# # Choose a port that is free
# PORT = 50000
#
# # An IPv4 address is obtained
# # for the server.
# SERVER = '127.0.0.1'
#
# # Address is stored as a tuple
# ADDRESS = (SERVER, PORT)
#
# # the format in which encoding
# # and decoding will occur
# FORMAT = "utf-8"
#
# # Lists that will contains
# # all the clients connected to
# # the server and their names.
# clients, names = [], []
#
# # Create a new socket for
# # the server
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # bind the address of the
# # server to the socket
# server.bind((SERVER,PORT))
#
#
# # function to start the connection
# def startChat():
#     print("server is working on " + SERVER)
#
#     # listening for connections
#     server.listen()
#
#     while True:
#         # accept connections and returns
#         # a new connection to the client
#         #  and  the address bound to it
#         conn, addr = server.accept()
#         conn.send("NAME".encode(FORMAT))
#
#         # 1024 represents the max amount
#         # of data that can be received (bytes)
#         name = conn.recv(1024).decode(FORMAT)
#
#         # append the name and client
#         # to the respective list
#         names.append(name)
#         clients.append(conn)
#
#         print(f"Name is :{name}")
#
#         # broadcast message
#         broadcastMessage(f"{name} has joined the chat!".encode(FORMAT))
#
#         conn.send('Connection successful!'.encode(FORMAT))
#
#         # Start the handling thread
#         thread = threading.Thread(target=handle,
#                                   args=(conn, addr))
#         thread.start()
#
#         # no. of clients connected
#         # to the server
#         print(f"active connections {threading.activeCount() - 1}")
#
#
# # method to handle the
# # incoming messages
# def handle(conn, addr):
#     print(f"new connection {addr}")
#     connected = True
#
#     while connected:
#         # receive message
#         message = conn.recv(1024)
#
#         # broadcast message
#         broadcastMessage(message)
#
#     # close the connection
#     conn.close()
#
#
# # method for broadcasting
# # messages to the each clients
# def broadcastMessage(message):
#     for client in clients:
#         client.send(message)
#
#
# # call the method to
# # begin the communication
# startChat()
from tkinter import *

HOST = '127.0.0.1'
PORT = 50000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen(15)
Socket_lst = []
nick_names = []


class server:
    def __init__(self):
        # chat server window
        self.window = Tk()
        self.window.withdraw()

        # login title
        self.login = Toplevel()
        self.login.title("Server")
        self.login.resizable(height=False,width=False)
        self.login.configure(width=500, height=500)


        # now we will create the label

        self.log = Label(self.login, text="Please start the server to continue", justify=CENTER, font="Ariel")
        self.log.place(relheight=0.15, relx=0.2, rely=0.07)

        self.textCons = Text(self.window, width=20, height=2, bg="#17202A", fg="#EAECEE", font="Helvetica 14", padx=4,pady=4)
        self.textCons.place(relheight=0.4, relwidth=1, rely=0.08)

        # now we will create the continue button
        self.continueB = Button(self.login, text="Start Server", font="Ariel", command=lambda: threading.Thread(target=self.server_chat()).start())
        self.stopB = Button(self.login, text="Stop Server", font="Ariel", command=lambda:threading.Thread(target=self.stop_server()).start())
        self.stopB.place(relx=0.5, rely=0.2)
        self.continueB.place(relx=0.2, rely=0.2)
        self.window.update_idletasks()
        self.window.mainloop()

    def stop_server(self):
        server_socket.close()

    def server_chat(self):
        print(" Server chat has been started successfully>>>" + HOST)
        while 1:
            print("Welcome to our chat room! , we are ready to go!")
            connectionSocket, addr = server_socket.accept()  # -> The accept method of Python's socket class,
            # accepts an incoming connection request from a TCP server <-
            connectionSocket.send('NickName?'.encode())
            name = connectionSocket.recv(1024)
            nick_names.append(name)
            Socket_lst.append(connectionSocket)
            print(f'{name} has been join'.encode())

            self.broadcast(f'{name} has been connect successfully!\n'.encode())
            connectionSocket.send('Welcome to our chat!'.encode())
            self.window.update_idletasks()
            self.continueB.update_idletasks()
            recv_thread = threading.Thread(target=self.clients_care, args=(connectionSocket, addr))
            recv_thread.start()

    # The aim of this function is to send message to all of the client in our server
    def broadcast(self,msg):
        for sock in Socket_lst:
            sock.send(msg)
            # self.window.update_idletasks()
            # self.continueB.update_idletasks()


# this function will help us to handle with connections and disconnection in our server
    def clients_care(self,client, address):

     while 1:
         try:
              msg = client.recv(1024)

              self.broadcast(msg)
              # self.window.update_idletasks()
              # self.continueB.update_idletasks()
         except:
              pos = Socket_lst.index(client)
              Socket_lst.remove(client)
              client.close()
              name = nick_names[pos]
              self.broadcast(f'{name} has been disconnected from the server!'.encode())
              nick_names.remove(name)
              # self.window.update_idletasks()
              # self.continueB.update_idletasks()
              break


# The aim of this function is to receive connection from the clients
# def recieve_connection():
#     while 1:
#         print("Welcome to our chat room! , we are ready to go!")
#         connectionSocket, addr = server_socket.accept()         # -> The accept method of Python's socket class,
#                                                                 # accepts an incoming connection request from a TCP server <-
#         connectionSocket.send('NickName?'.encode())
#         name = connectionSocket.recv(1024)
#         nick_names.append(name)
#         Socket_lst.append(connectionSocket)
#         print(f'{name} has been join'.encode())
#
#         broadcast(f'{name} has been connect successfully!\n'.encode())
#         connectionSocket.send('Welcome to our chat!'.encode())
#         recv_thread = threading.Thread(target=clients_care, args=(connectionSocket,))
#         recv_thread.start()
#         ####################################################################################################################
# connectionSocket.send('Show Online'.encode())
# online = connectionSocket.recv(1024)
# if online == 'Show Online':
#     broadcast(f'There are {len(Socket_lst)} members in the chat')
#     print(f"There are {len(Socket_lst)} in here")
# else:
#     continue
# connectionSocket.send('Show Online'.encode())
# online_members = connectionSocket.recv(1024)
#
# broadcast(f'There are {online_members} Online members'.encode())
# print(f'There are {len(Socket_lst)} Online members'.encode())
#
#
# def show_online():
#     while 1:
#         print("cadsvwebvwerv")
#         connectionSocket, addr = server_socket.accept()
#         connectionSocket.send('Show Online'.encode())
#         online_members = connectionSocket.recv(1024)
#         if online_members == 'Online':
#             broadcast(f'There are {len(Socket_lst)} Online members'.encode())
#             print(f'There are {len(Socket_lst)} Online members'.encode())
#         else:
#             break
# #         online_thread = threading.Thread(target=recieve_connection())
# #         online_thread.start()

if __name__ == '__main__':
    server()
