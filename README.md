What it does?

  The goal of this project was to use Python’s socket and threading libraries to create a terminal based messaging tool with legitimate functionality and merritt. This client-server program allows for communication of messages between clients connected to the same server. The program as a whole relies on the server to keep track of essential information and handle simultaneous client connection and the client for a fluid user experience. The clients never directly interact with one another and instead use the server as a kind of data hub. The clients and server are always bouncing back and forth between one another - one sends data and the other responds accordingly. 

How to use?

  First, make sure the server is properly running. To do this make sure it is running in a terminal and it will alert you accordingly. Next, make sure that the client program is being run in a manner that it can reach the server program. Once a client is running and properly connected to the server it will alert you accordingly. The user interface will then guide you through the process of usable commands and selecting your username. In order to add additional clients connect them in the same manner as the first client. In order to disconnect terminate the client program being run in the terminal. 

Known bugs/limitations?

  The largest known bug is a potential for a stall between the termination of the server program and the ability to run a new iteration of it. Sometimes, upon trying this you will be greeted with the error that the server identifiers are already in use. This usually resolves itself in a quick amount of time, but may sometimes require a change of the hardcoded port numbers in the client and server code. 

What would I add?

  One thing I would add is some sort of broadcast command which allows for a message from a client to be sent to all other clients currently connected to the server. Another large change I might consider to the nature of the program is the threading of the clients to allow for the simultaneous real time receiving and sending of messages. This shift would cause the program to more resemble texting than email but would hopefully significantly improve the user experience. Two final, smaller things I might add are the ability for the user to input the server address they are trying to connect to upon starting the client program and a rethinking of the command names. 
