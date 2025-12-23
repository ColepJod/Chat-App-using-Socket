import socket
import threading
import sys

SERVER_HOST = "127.0.0.1"   # yahan server ki IP daal
SERVER_PORT = 5000


def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("\nServer disconnected.")
                break
            print("\nServer:", data.decode("utf-8"))
            print("You: ", end="", flush=True)
        except Exception:
            break


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((SERVER_HOST, SERVER_PORT))
    except Exception as e:
        print(f"Could not connect: {e}")
        sys.exit(1)

    print(f"Connected to {SERVER_HOST}:{SERVER_PORT}")
    print("Type /quit to exit.")

    t = threading.Thread(target=receive_messages, args=(s,), daemon=True)
    t.start()

    try:
        while True:
            msg = input("You: ")
            if msg.strip().lower() == "/quit":
                break
            if not msg:
                continue
            s.sendall(msg.encode("utf-8"))
    except KeyboardInterrupt:
        pass
    finally:
        s.close()
        print("\nConnection closed.")


if __name__ == "__main__":
    main()
