import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5500))

    while True:
        msg = input("Enter message: ")
        client.send(msg.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(f"Server: {response}")

if __name__ == "__main__":
    start_client()
