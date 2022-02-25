import socket
import sys
import threading
import socket
from tkinter import *

#all of this parameters are related to our client socket
HOST = '127.0.0.1'
PORT = 50000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


# this class will be our gui class
class Chat:

    def __init__(self):

        # chat window which is currently hidden
        self.window = Tk()
        self.window.withdraw()

        # login window
        self.login = Toplevel()
        # set the title
        self.login.title("Login")
        self.login.resizable(width=True, height=True)
        self.login.configure(width=400, height=300)



        # creating the login label inside our window
        self.log = Label(self.login, text="Please login to continue", justify=CENTER, font="Ariel")

        self.log.place(relheight=0.15, relx=0.2, rely=0.07)
        # create a Label
        self.labelName = Label(self.login, text="Nickname: ", font="Helvetica 12")

        self.labelName.place(relheight=0.2, relx=0.1, rely=0.2)

        # Now we will create the entrybox
        self.entrybox = Entry(self.login, font="Helvetica 14")

        self.entrybox.place(relwidth=0.4, relheight=0.12, relx=0.35, rely=0.2)
        self.entrybox.focus()

        # now we will create the continue button
        self.continueB = Button(self.login, text="CONTINUE", font="Ariel", command=lambda: self.goAhead(self.entrybox.get()))
        self.continueB.place(relx=0.4, rely=0.55)


        self.window.mainloop()

    def goAhead(self, name):
        self.login.destroy()
        self.layout(name)

        # the thread to receive messages
        recieve = threading.Thread(target=self.receive)
        recieve.start()

    # The main layout of the chat
    def layout(self, name):

        self.name = name
        # to show chat window
        self.window.deiconify()
        self.window.title("CHATROOM")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=600, height=600,bg="#17202A")

        self.labelHead = Label(self.window, bg="#17202A", fg="#EAECEE", text=self.name,font="Helvetica 13 bold", pady=5)
        self.labelHead.place(relwidth=1)

        self.line = Label(self.window, width=450, bg="#ABB2B9")

        self.line.place(relwidth=1,rely=0.07, relheight=0.012)

        self.textCons = Text(self.window, width=20, height=2, bg="#17202A",fg="#EAECEE",font="Helvetica 14", padx=4,pady=4)
        self.textCons.pack(pady=5)
        self.textCons.place(relheight=0.4,relwidth=1, rely=0.08)

        self.labelBottom = Label(self.window, bg="#ABB2B9",height=80)
        self.labelBottom.place(relwidth=1,rely=0.5)

        self.entryMsg = Entry(self.labelBottom,bg="#2C3E50",fg="#EAECEE",font="Helvetica 13")

        # place the given widget
        # into the gui window
        self.entryMsg.place(relwidth=0.4, relheight=0.08, rely=0.010, relx=0.011)
        self.entryMsg.focus()

        self.privatMsg= Entry(self.labelBottom, bg="#2C3E50",fg="#EAECEE",font="Helvetica 13")
        self.privatMsg.place(relwidth=0.3, relheight=0.075, rely=0.09, relx=0.011)
        self.privatMsg.focus()
        # create a Send Button
        self.buttonMsg = Button(self.labelBottom, text="Send", font="Helvetica 10 bold",width=20,bg="#ABB2B9",command=lambda:threading.Thread(self.sendButton(self.entryMsg.get())).start())
        self.buttonMsg.place(relx=0.5,rely=0.008,relheight=0.06,relwidth=0.22)
        self.show_onlineB= Button(self.labelBottom,text="Show Online", font="Helvetica 10 bold",width=20,bg="#ABB2B9" )
        self.show_onlineB.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        self.privateB = Button(self.labelBottom, text= "Private Message", font="Helvetica 10 bold",bg="#ABB2B9")
        self.privateB.place(relx=0.5, rely=0.087, relheight= 0.06, relwidth=0.22, )
        self.showFilesB = Button(self.labelBottom, text= "Show Files",font="Helvetica 10 bold",bg="#ABB2B9")
        self.showFilesB.place(relx=0.77, rely=0.087, relheight=0.06, relwidth=0.22, )

        self.clearB = Button(self.labelBottom, text="Clear Chat", font="Helvetica 10 bold",bg="#ABB2B9",command= lambda:self.clear_chat())
        #self.clearB.pack()
        self.clearB.place(relx=0.77, rely=0.16, relheight=0.06, relwidth=0.22)
        #self.textCons.update()
        # self.privatentry = Entry(self.labelBottom,bg="#2C3E50",fg="#EAECEE",font="Helvetica 13")
        # self.entryMsg.place(relwidth=0.07, relheight=0.008, rely=0.010, relx=0.011)

        self.textCons.config(cursor="arrow")


        #create a scroll bar
        scrollbar = Scrollbar(self.textCons)

        # place the scroll bar
        # into the gui window
        scrollbar.place(relheight=1,relx=0.974)

        scrollbar.config(command=self.textCons.yview)

        self.textCons.config(state=DISABLED)
    def show_online(self):
        client_socket.send("show online".encode())


    def clear_chat(self):
        self.textCons.configure(state=NORMAL)
        self.textCons.delete('1.0',END )
        self.textCons.configure(state=DISABLED)


    # function to basically start the thread for sending messages
    def sendButton(self, msg):
        self.textCons.config(state=DISABLED)
        self.msg = msg
        self.entryMsg.delete(0, END)
        snd = threading.Thread(target=self.sendMessage)
        snd.start()

    # function to receive messages
    def receive(self):
        while True:
            try:
                message = client_socket.recv(1024).decode()

                # if the messages from the server is NAME send the client's name
                if message == 'NAME':
                    client_socket.send(self.name.encode())
                else:
                    # insert messages to text box
                    self.textCons.config(state=NORMAL)
                    self.textCons.insert(END, message + "\n\n")

                    self.textCons.config(state=DISABLED)
                    self.textCons.see(END)
            except:
                # an error will be printed on the command line or console if there's an error
                print("An error occured!")
                client_socket.close()
                break

    # function to send messages
    def sendMessage(self):
        self.textCons.config(state=DISABLED)
        while True:
            message = (f"{self.name}: {self.msg}")
            client_socket.send(message.encode())
            print(client_socket.type)
            break

        # create a GUI class object


chat = Chat()

