import threading
import socket


def client():
    
    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 12001

    try:
        socket_instance = socket.socket()
        socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))

        ##Print out usable commands sent to client by server
        print("Connected To The Server!")
        print("Usable Commands:")
        commands = socket_instance.recv(1024).decode()
        commands_list = commands.split(",")
        for command in commands_list:
            print(command)
        print("...")

        invalid_username = True

        #Username declaration loop. Continues until newly server accepts clients unique username
        while invalid_username:

            print("Enter Your Username: ")
            client_username_input = input()
            socket_instance.send(client_username_input.encode())
            username_response = socket_instance.recv(1024)

            if username_response.decode() == "INVALID_USERNAME":
                print("ERROR: Username Already In Use")
            else:
                client_username = client_username_input
                print("Welcome!")
                break
        
        terminal_message = (client_username + " ==> ")
        
        ##Client terminal loop. Sends messages to server and waits for the according response
        while True:
            msg = input(terminal_message)
            socket_instance.send(msg.encode())
            response_msg = socket_instance.recv(1024)

            ##Check if the type of message sent by the server is special, else print message as is
            if (response_msg.decode()[:11] == "TAG == CMDR"):
                commands_list = response_msg.decode()[11:].split(",")
                for command in commands_list:
                    print(command)
            if (response_msg.decode()[:11] == "TAG == MLBX"):
                inbox_list = response_msg.decode()[11:].split(",")
                for inbox_entry in inbox_list:
                    print(inbox_entry)
            else:
                print(response_msg.decode())


    ##Exception is raised if client cannot connect to server
    except Exception as e:
        print(f'Error connecting to server socket {e}')
        socket_instance.close()


if __name__ == "__main__":
    client()
