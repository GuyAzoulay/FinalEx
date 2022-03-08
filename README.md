# Final Task- Communication between client and server
* Written by Guy Azoulay and Batel Cohen

## main goal of the project-

In this assigment we asked to built a communication app between multiply client and one server,
we tried our best to achieve our main goal: an application with basic gui which with it we could communicate
each other with messages, private messages and file download and upload.
While exploring this field and programming it we achieve a good and deep understanding
about all the communication world, how binding between differnt clients and server work,
what is happening in the background of it etc.
We wont lie, at first it was a little bit hard to understand how to make all of this work as
we want, but giccing up was not a option, so we sat and learned every part in this assigment
not just for an A in our final grade, we also improved our knowledge in this field.

In this assigment we implemented two main classes:
* server
* client including a gui

## Explanation about the Server class:

This class is the main class in our project, everything which send from any client
is going through the server, and server provide any action we would like to do.
Our main host IP is 127.0.0.1 and the port we work on is 50,000 as we asked for.
All the communication work via TCP connection, messages, private messages, online members and etc.
In aim to transfer files we created anothe sochet which work via UDP connection,
we asked to implement it using RDP.
Every new client which entered to our chat is addint to two lists:

* The first one is nickname fields.
* The seconed one is the socket which the client connected to our socket.

At first we created a class which hold the UDP port, which work with 3 main variables:
* Available : this parameter is boolean and will help us to know if some port is free to use.
* Client_Address : what is the client address we would to connect to.
* Sock : the UDP socket we connected to.

All the other function in this section will help us farther in this project
with the file transfer, function like:
* addport
* remover port
* get available port 

###### Note!- all of the previous is related to the file transfer!

### The boradcast function

One of the most improtent function in our project is the broadcast, 
it might seem a little bit simple but most of the communication is
usnig this function.
This function is going through all the clients's socket and send the messages to all
the members which are online via the send function.

### The receive function

This function working in an endless loop.
First, it using the accept method, which accepet an incoming connection request
from TCP server.
It asking our client for Nickname and adding it nickname to our nickname list
and with the accept function we are getting the specific client socket and ass it to the
client socket list.
Than we add a thread to the function which will work on the handle class.

### The handle function

The main goal of this function is to handle with all the requsts which we
get from the server class.
We are handling with commend such as:

* Send message
* Send private message
* Show online members
* Show files
* Download files

For every commend from the client we implemented a different implimitation
in aim to answer on every client's request.

## Explanation on the Client class

This class represents our clients, every new client which want to communicate
via our server is going through this class.
It was a little bit difficult to dipply understand how different classes
communicate with each othe via commend, after we researched in which
library of gui we want to use, we use the Tkinter library.

### The show online function

This function is showing all the inline members in our chat.

### The write function

This function is handling with everything we write in our text bar 
and sending it to the server which using the broadcast function to
send all the information to the othe clients.

### The stop function

This function send to the server a message when a client is disconnect
from our server.

### The askFile function

This function aim is the send a request to the server for a specific
file.

### The recieved function

This function is one of the most importent function in the client class,
in it we get all the answers from the server and replied to it.

### The recievedFile function

This function main aim is to handle with a file which we asked for from the sever
and read it byte after byte.

### The login function

When a new client is connect to our server via the login button we want
him to connect to our server.

## How to run

In aim to run the code, we run it via an exe file,
At first we need to run the the server:





