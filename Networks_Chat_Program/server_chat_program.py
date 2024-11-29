import socket, threading

class Server:

    def __init__(self):

        #Instance variable declarations
        LISTENING_PORT = 12001
        self.clients = {}
        self.client_inboxes = {}
        self.client_usernames = []
        self.commands = ["Client-Dir; - Gives List Of Client Usernames Connected To Server",
                         "Cmd-Dir; - Gives List Of Usable Commands",
                         "Send-Message;<USERNAME> Message - Send A Message To A User Connected To The Server",
                         "View-Messages; - View All Current Messages In Your Inbox",
                         "Clear-Messages; - Clear All Current Messages In Your Inbox",]
        
        
        try:

            #Try creating socket instance of the server for clients to connect to
            socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_instance.bind(('', LISTENING_PORT))
            socket_instance.listen()

            print('Server running!')
            
            #Server loop
            while True:

                socket_connection, address = socket_instance.accept()

                #Create a thread for each new user that connects in order to handle simultanious connections
                threading.Thread(target= self.handle_user_connection, args=[socket_connection, address]).start()
                
        
        #Exception arrises if server can not succesfuly be created
        except Exception as e:
            print(f'An error has occurred when instancing socket: {e}')
            socket_connection.close()
            

    def handle_user_connection(self, connection: socket.socket, address: str):

        #Send newly connected client available commands
        connection.send(str(self.commands).encode())

        #Username declaration loop. Continues until newly connected client picks a unique username or connection interupted 
        while True:

            try:

                msg = connection.recv(1024)
                client_username = msg.decode()
                if client_username in self.client_usernames:
                    connection.send("INVALID_USERNAME".encode())
                else:
                    connection.send("VALID_USERNAME".encode())
                    self.clients[client_username] = connection
                    self.client_inboxes[client_username] = []
                    self.client_usernames.append(client_username)
                    break
            
            #Exception arrises if Server-Client connection interupted. Client erased from server
            except Exception as e:
                print(f'Error to handle user connection: {e}')
                print(client_username, " Has Disconnected")
                del self.clients[client_username]
                self.client_usernames.remove(client_username)
                break
            
        
        #Server-Client client input loop. Checks if client has sent a valid command and responds accordingly.
        while True:
            
            try:

                msg = connection.recv(1024)
                print("Recieved ", msg, "From ", client_username)

                if (msg.decode() == "Client-Dir;"):
                    connection.send(str(self.client_usernames).encode())
                elif (msg.decode() == "Cmd-Dir;"):
                    ##TAG addition helps client know how to format certain specific kinds of data it recieves
                    connection.send("TAG == CMDR".encode() + str(self.commands).encode())
                elif (msg.decode()[:13] == "Send-Message;"):
                    if (">" not in msg.decode() or "<" not in msg.decode()):
                        connection.send("ERROR: Invalid Command".encode())
                    elif msg.decode()[14:(msg.decode().find(">"))] not in self.client_usernames:
                        connection.send("ERROR: Invalid Username".encode())
                    elif msg.decode()[14:(msg.decode().find(">"))] == client_username:
                        connection.send("ERROR: Cannot Send Message To Yourself".encode())
                    else:
                        sending_username = msg.decode()[14:(msg.decode().find(">"))]
                        self.client_inboxes[sending_username].append(client_username.upper() + ": " + 
                                                                     msg.decode()[msg.decode().find(">") + 1:])
                        connection.send("Message Sent!".encode())
                elif (msg.decode() == "View-Messages;"):
                    connection.send("TAG == MLBX".encode() + str(self.client_inboxes[client_username]).encode())
                elif (msg.decode() == "Clear-Messages;"):
                    self.client_inboxes[client_username].clear()
                    connection.send("Messages Cleared!".encode())
                else:
                    connection.send("ERROR: Invalid Command".encode())

            #Exception arrises if Server-Client connection interupted. Client erased from server
            except Exception as e:
                print(f'Error to handle user connection: {e}')
                print(client_username, " Has Disconnected")
                del self.clients[client_username]
                self.client_usernames.remove(client_username)
                break


if __name__ == "__main__":
    server = Server()
