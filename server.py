import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5500))
    server.listen(5)
    print("Server is listening on port 5500...")

    while True:
        client, address = server.accept()
        print(f"Connection from {address} has been established.")

        while True:
            msg = client.recv(1024).decode('utf-8')
            if not msg:
                break
            print(f"Received: {msg}")
            client.send("Message received".encode('utf-8'))

        client.close()

if __name__ == "__main__":
    start_server()
