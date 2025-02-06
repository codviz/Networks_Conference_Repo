import socket
# hi friend just making a comement

def client():
    
    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 12000

    try:
        socket_instance = socket.socket()
        socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))

        print('Connected To The Server!')
        print("Guess A Number Between 0 and 4, Type 'Quit' To Disconnect From Server: " )

        while True:

            guess = input()
            socket_instance.send(guess.encode())

            msg = socket_instance.recv(1024)
            print(msg.decode())

            if input == "quit":
                socket_instance.close()
                break
                
    except Exception as e:
        print(f'Error connecting to server socket {e}')
        socket_instance.close()


if __name__ == "__main__":
    client()
