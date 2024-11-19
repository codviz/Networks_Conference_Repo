import socket


def client():
    
    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 12000

    try:
        socket_instance = socket.socket()
        socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))

        print("Connected To The Server!")
        print("Usable Commands:")
        print(socket_instance.recv(1024).decode())
        print("...")

        invalid_username = True

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
        
        terminal_message = (client_username + " ==>")

        while True:
            msg = input(terminal_message)
            socket_instance.send(msg.encode())
            response_msg = socket_instance.recv(1024)
            print(response_msg.decode())

            
                
    except Exception as e:
        print(f'Error connecting to server socket {e}')
        socket_instance.close()


if __name__ == "__main__":
    client()
